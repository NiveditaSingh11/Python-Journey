import requests

response = requests.get("https://api.github.com")
print(response)
print(response.status_code)
print(response.headers) #returns json object
print(response.headers['Date'])
print(response.headers['Content-Type'])
print(response.json())
print((response.json()['current_user_url']))
