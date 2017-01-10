import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/sam9116/cmput404-lab1/master/lab1.py")

print response.status_code
print response.text


