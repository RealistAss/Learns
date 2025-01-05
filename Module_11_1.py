import requests as rq

GetParams = {'param1': 'value1', 'param2': 'value2'}
response = rq.get('https://google.com', GetParams)

print(response.url)

response = rq.head('https://google.com', timeout=2)

print(response.headers)