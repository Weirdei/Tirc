# I will try to use urllib3 without framework in study purposes

import urllib3
import json
from pprint import pprint
import ssl
import certifi

BASE_API = 'https://api.telegram.org'
API_KEY = 'bot323157985:AAH6_R0PyQemilBWZ4RsV9ttzfvDDqgourA'


http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
)

def method_to_url(method):
    return (BASE_API + '/' + API_KEY + '/' + method)

try:
    request = http.request('GET', method_to_url('getUpdates'))
except urllib3.exceptions.SSLError as e:
    pprint(e)

response = json.loads(request.data.decode('utf-8'))

pprint(response['result'])







