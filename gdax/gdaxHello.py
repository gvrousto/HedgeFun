import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import websocket


# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.gdax.com/'
API_KEY = 'd1b7ae5ace66f085968eda069e9b8045'
API_SECRET = 'KFv4Szkc83J3vOZq9Irhmsets4A8R1hsgxEvN9/rv7a53Pc77So/sm4S4DYe4fbT7qhPZAeaVjIyCxW62pc2yA=='
API_PASS = 'aloevera10'

auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

# Get accounts
r = requests.get(api_url + 'accounts', auth=auth)
print r.json()
print('balances')
for index in r.json():
	print index['balance']
# [{"id": "a1b2c3d4", "balance":...


const ws = new Gdax.WebsocketClient(['LTC-USD']);

ws.on('message', function(data) { 
	/* work with data */ 
	if (data['type'] == 'received') {
		console.log(data);	
	}
});

