# Python bindings for Quoinex/Qryptos API

Mirrors the endpoints as documented on https://developers.quoine.com/.
Note: Use at your own risk.

## Dependencies
- requests
- pyjwt

## Usage

1. Acquire your API token id and passpharse from the platform's setting page
2. Set platform of choice
    '''
        # Instantiating for Quoinex platform
        api = Quoine(token_id, token_passphrase)

        # Instantiating for Qryptos platform
        api = Quoine(token_id, token_passphrase, is_qryptos=True)
    '''
3. Example code
    '''
        #!/usr/bin/env python
        from python-quoine import Quoine

        token_id = 'REPLACE_WITH_TOKEN_ID'
        token_passphrase = 'REPLACE_WITH_TOKEN_PASSPHRASE'

        api = Quoine(token_id, token_passphrase, is_qryptos=True)
        resp = api.get_products()

        print(resp.status_code)
        print(resp.content)
    '''

#### Feel free to tip :)

- BTC: 133x9Rb7ABbgTg89wmoVWJibxuiWkSZXB9
- LTC: LYbUbs5tMAv6tDapH8GFvAAfsxVxz4VeYE
- ETH: 0x467A9b9cf150F939008ad819dC4daaF0a1815643

## Licence

MIT License

Copyright (c) 2017 Sean Lim

See [LICENSE.md](LICENSE.md)
