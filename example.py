from quoine import Quoine

token_id = 'REPLACE_WITH_TOKEN_ID'
token_passphrase = 'REPLACE_WITH_TOKEN_PASSPHRASE'

api = Quoine(token_id, token_passphrase)
resp = api.get_products()

print(resp.status_code)
print(resp.content)
