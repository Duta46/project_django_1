from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
import requests
import hashlib
from datetime import datetime
from .models import Produk, Kategori, Status
from .forms import ProdukForm
from .serializers import ProdukSerializer, KategoriSerializer, StatusSerializer
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_api_data():
    # Use the provided username and password
    username = "tesprogrammer310126C15"
    password_md5 = "2a6fdc460dd5afb285d3a5b10aa50df0"

    # API endpoint
    api_url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    # Request headers (without Content-Type to let requests set it appropriately for form data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Request payload as form data instead of JSON
    payload = {
        'username': username,
        'password': password_md5
    }

    try:
        print(f"Mengirim permintaan ke {api_url}")
        print(f"Payload: {payload}")

        # Disable SSL verification due to certificate issues
        response = requests.post(api_url, headers=headers, data=payload, verify=False, timeout=30)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text[:500]}...")  # Print first 500 chars

        response.raise_for_status()
        api_response = response.json()
        print(f"API Response keys: {api_response.keys()}")

        # Convert API response to expected format
        if 'data' in api_response:
            converted_data = convert_api_response(api_response['data'])
            print(f"Converted {len(converted_data['produk'])} products")
            return converted_data

        print("Tidak menemukan 'data' dalam respons API")
        return None
    except requests.exceptions.Timeout:
        print("Timeout saat mengakses API")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Kesalahan koneksi saat mengakses API: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error saat mengakses API: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except ValueError as e:  # JSON decode error
        print(f"Error decoding JSON response: {e}")
        print(f"Response text: {response.text}")
        return None


def convert_api_response(api_data):
    """
    Convert API response to the expected format
    """
    # Extract unique categories and statuses from the API data
    categories = {}
    statuses = {}
    products = []

    for item in api_data:
        # Add category if not exists
        if item['kategori'] not in categories:
            categories[item['kategori']] = len(categories) + 1

        # Add status if not exists
        if item['status'] not in statuses:
            statuses[item['status']] = len(statuses) + 1

        # Create product entry
        product = {
            'id_produk': int(item['id_produk']),
            'nama_produk': item['nama_produk'],
            'harga': int(item['harga']) if item['harga'].isdigit() else 0,
            'kategori_id': categories[item['kategori']],
            'status_id': statuses[item['status']]
        }
        products.append(product)

    # Convert dictionaries to list format
    categories_list = [{'id_kategori': v, 'nama_kategori': k} for k, v in categories.items()]
    statuses_list = [{'id_status': v, 'nama_status': k} for k, v in statuses.items()]

    return {
        'kategori': categories_list,
        'status': statuses_list,
        'produk': products
    }



def sync_produk_from_api(request):
    """
    Fetch data from API and save to database
    """
    api_data = get_api_data()

    if not api_data:
        messages.error(request, "Gagal mengambil data dari API. Silakan coba lagi nanti.")
        return redirect('produk_list')

    try:
        # Process categories
        for category_data in api_data.get('kategori', []):
            Kategori.objects.update_or_create(
                id=category_data['id_kategori'],
                defaults={
                    'nama_kategori': category_data['nama_kategori']
                }
            )

        # Process statuses
        for status_data in api_data.get('status', []):
            Status.objects.update_or_create(
                id=status_data['id_status'],
                defaults={
                    'nama_status': status_data['nama_status']
                }
            )

        # Process products
        for product_data in api_data.get('produk', []):
            # Get or create related objects to avoid issues with get() returning multiple objects
            kategori_obj, created = Kategori.objects.get_or_create(
                id=product_data['kategori_id'],
                defaults={'nama_kategori': 'Unknown Category'}
            )

            status_obj, created = Status.objects.get_or_create(
                id=product_data['status_id'],
                defaults={'nama_status': 'Unknown Status'}
            )

            Produk.objects.update_or_create(
                id=product_data['id_produk'],
                defaults={
                    'nama_produk': product_data['nama_produk'],
                    'harga': product_data['harga'],
                    'kategori': kategori_obj,
                    'status': status_obj
                }
            )

        messages.success(request, "Data berhasil disinkronisasi dari API")
    except Exception as e:
        messages.error(request, f"Terjadi kesalahan saat menyimpan data: {str(e)}")

    return redirect('produk_list')

def produk_list(request):
    """
    Display products with status "bisa dijual"
    """
    # Get the status object for "bisa dijual"
    # Handle case where multiple objects exist
    try:
        # Try to get the status object directly
        bisa_dijual_status = Status.objects.get(nama_status="bisa dijual")
    except Status.MultipleObjectsReturned:
        # If multiple objects exist, get the first one
        bisa_dijual_status = Status.objects.filter(nama_status="bisa dijual").first()
    except Status.DoesNotExist:
        # If no object exists, create it
        bisa_dijual_status = Status.objects.create(nama_status="bisa dijual")

    # Get products with status "bisa dijual"
    if bisa_dijual_status:
        produk_list = Produk.objects.filter(status=bisa_dijual_status)
    else:
        produk_list = Produk.objects.none()

    context = {
        'produk_list': produk_list
    }
    return render(request, 'produk/list.html', context)

def produk_create(request):
    """
    Create a new product
    """
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil ditambahkan")
            return redirect('produk_list')
    else:
        form = ProdukForm()

    context = {
        'form': form,
        'action': 'Tambah'
    }
    return render(request, 'produk/form.html', context)

def produk_update(request, pk):
    """
    Update an existing product
    """
    produk = get_object_or_404(Produk, pk=pk)

    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diperbarui")
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)

    context = {
        'form': form,
        'action': 'Edit'
    }
    return render(request, 'produk/form.html', context)

def produk_delete(request, pk):
    """
    Delete a product
    """
    produk = get_object_or_404(Produk, pk=pk)

    if request.method == 'POST':
        produk.delete()
        messages.success(request, "Produk berhasil dihapus")
        return redirect('produk_list')

    context = {
        'produk': produk
    }
    return render(request, 'produk/delete_confirmation.html', context)