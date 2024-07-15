import requests

# Define the base URL of your Flask API
base_url = 'http://localhost:5000'

# Example: Testing the /api/endpoint GET endpoint
def test_api_endpoint():
    url = f'{base_url}/api/endpoint'
    response = requests.get(url)

    # Check the response status code
    assert response.status_code == 200

    # Optionally, check the response content
    print(response.json())  # Print JSON response

# Example: Testing the /register POST endpoint
def test_register():
    url = f'{base_url}/register'
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = requests.post(url, json=data)

    # Check the response status code
    assert response.status_code == 201

    # Optionally, check the response content
    print(response.json())  # Print JSON response

# Example: Testing the /login POST endpoint
def test_login():
    url = f'{base_url}/login'
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = requests.post(url, json=data)

    # Check the response status code
    assert response.status_code == 200

    # Optionally, check the response content
    print(response.json())  # Print JSON response

# Example: Testing the /account GET endpoint (requires authentication)
def test_account():
    url = f'{base_url}/account'
    # Assuming you have a valid access token to test with
    headers = {'Authorization': 'Bearer <your_access_token>'}
    response = requests.get(url, headers=headers)

    # Check the response status code
    assert response.status_code == 200

    # Optionally, check the response content
    print(response.json())  # Print JSON response

# Example: Testing the /transaction POST endpoint (requires authentication)
def test_transaction():
    url = f'{base_url}/transaction'
    data = {
        'from_account_id': 1,
        'to_account_id': 2,
        'amount': 100
    }
    # Assuming you have a valid access token to test with
    headers = {'Authorization': 'Bearer <9459bf626aefd220092bf0cc3b94eacb7cb42e0e547d9ffa>'}
    response = requests.post(url, json=data, headers=headers)

    # Check the response status code
    assert response.status_code == 201

    # Optionally, check the response content
    print(response.json())  # Print JSON response

# Run all test functions
if __name__ == '__main__':
    test_api_endpoint()
    test_register()
    test_login()
    test_account()
    test_transaction()
