# Quoinex/Qryptos Python Client

Python binding for Quoinex/Qryptos API v2.
Bindings mirrors the endpoints as documented on https://developers.quoine.com/.

Note: Use at your own risk.

# Usage

1. Acquire your API token id and passpharse from the platform's setting page
2. Set the platform of choice

    #!/usr/bin/env python
    from python-quoine import Quoine

    token_id = 'REPLACE_WITH_TOKEN_ID'
    token_passphrase = 'REPLACE_WITH_TOKEN_PASSPHRASE'

    api = Quoine(token_id, token_passphrase)
    resp = api.get_products()

    print(resp.status_code)
    print(resp.content)


Feel free to tip :)

BTC: 133x9Rb7ABbgTg89wmoVWJibxuiWkSZXB9
LTC: LYbUbs5tMAv6tDapH8GFvAAfsxVxz4VeYE
ETH: 0x467A9b9cf150F939008ad819dC4daaF0a1815643

## Licence

MIT License

Copyright (c) 2017 Sean Lim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
