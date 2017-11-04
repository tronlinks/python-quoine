from quoine import Quoine

token_id = ''
user_secret = ''

api = Quoine(token_id, user_secret)
resp = api.get_products()

print(resp.status_code)
print(resp.content)
