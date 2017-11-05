from quoine import Quoine

token_id = 'REPLACE_WITH_TOKEN_ID'
token_passphrase = 'REPLACE_WITH_TOKEN_PASSPHRASE'

api = Quoine(token_id, token_passphrase)

status, result = api.get_products()
print(status, result)

status, result = api.get_product(5)
print(status, result)

status, result = api.get_order_book(5)
print(status, result)

status, result = api.get_executions(5)
print(status, result)

status, result = api.get_interest_rates('USD')
print(status, result)

status, result = api.get_own_executions(5)
print(status, result)
