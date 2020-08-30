import requests
re = requests.get('https://ifconfig.me/ip')
print(re.text)