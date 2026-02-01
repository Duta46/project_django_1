import requests

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

print(f"Mengirim permintaan ke {api_url}")
print(f"Headers: {headers}")
print(f"Payload: {payload}")

try:
    # Disable SSL verification due to certificate issues
    response = requests.post(api_url, headers=headers, data=payload, verify=False, timeout=30)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    if response.status_code == 200:
        api_response = response.json()
        print(f"API Response: {api_response}")
    else:
        print(f"Permintaan gagal dengan status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except ValueError as e:  # JSON decode error
    print(f"Error decoding JSON response: {e}")
    print(f"Response text: {response.text}")