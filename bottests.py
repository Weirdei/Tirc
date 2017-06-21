
import urllib3
import json
from pprint import pprint
import ssl
import certifi

BASE_API = 'https://api.telegram.org'
API_KEY = 'bot323157985:AAH6_R0PyQemilBWZ4RsV9ttzfvDDqgourA'

MESSAGE_ID_CONTAINER_FILENAME = 'message_id_container'



http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
)



def read_update_id(filename):
    with open(filename) as f:
        return int(f.read())


def write_update_id(filename, num):
    with open(filename, 'w') as f:
        f.write(num)

class Bot:

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def method_to_url(self, method):
        return self.base_url + '/' + self.api_key + '/' + method

    def call_method(self, method):
        request =



bot = Bot(API_KEY, BASE_API)

