"""
(Unofficial) Python binding for Quoinex/Qryptos API v2.
See https://developers.quoine.com/ for more information

"""

import time
import json
import jwt
import requests
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

BASE_URL_QUOINEX = 'https://api.quoine.com/'
BASE_URL_QRYPTOS = 'https://api.qryptos.com/'


class Quoine:
    def __init__(self, token_id, token_secret, is_qryptos=False):
        self.token_id = str(token_id)
        self.token_secret = str(token_secret)
        if is_qryptos:
            self.base_url = BASE_URL_QRYPTOS
        else:
            self.base_url = BASE_URL_QUOINEX

    def api_request(self, request_type, path, params=None):
        # prep headers
        auth_payload = {
            'path': path,
            'nonce': str(int(time.time())),
            'token_id': self.token_id
        }

        encoded_jwt = jwt.encode(auth_payload, self.token_secret,
                                 algorithm='HS256')

        request_headers = {
            'X-Quoine-API-Version': '2',
            'X-Quoine-Auth': encoded_jwt,
            'Content-Type': 'application/json'
        }

        # make request
        request_url = self.base_url + path

        if request_type == 'GET':
            if params is not None and params is not {}:
                request_url += '?' + urlencode(params)

            resp = requests.get(request_url, headers=request_headers)

        elif request_type == 'PUT':
            if params is not None:
                payload = json.dumps(params)
            else:
                payload = None

            resp = requests.put(request_url, headers=request_headers,
                                data=payload)

        elif request_type == 'POST':
            if params is not None:
                payload = json.dumps(params)
            else:
                payload = None

            resp = requests.post(request_url, headers=request_headers,
                                 data=payload)

        # parse results
        result = None
        try:
            result = json.loads(str(resp.content, 'utf-8'))
        except Exception:
            result = str(resp.content, 'utf-8')

        return resp.status_code, result

    # Products (Public API)
    def get_products(self):
        """
        Get the list of all available products
        """

        return self.api_request('GET', 'products')

    def get_product(self, product_id):
        """
        Get a product
        """

        return self.api_request('GET', 'products/{}'.format(product_id))

    def get_order_book(self, product_id, full=False):
        """
        Get price levels of a product
        """
        params = {}
        if full:
            params['full'] = 1

        return self.api_request('GET', 'products/{}/price_levels'.format(
                                product_id), params)

    # Executions (Public API)
    def get_executions(self, product_id, limit=None,
                       page=None, timestamp=None):
        """
        Get a list of recent executions from a product
        (Executions are sorted in DESCENDING order - Latest first)
        """
        params = {
            'product_id': product_id
        }
        if limit is not None:
            params['limit'] = limit
        if page is not None:
            params['page'] = page
        if timestamp is not None:
            params['timestamp'] = timestamp

        return self.api_request('GET', 'executions', params)

    # Interest Rates (Public API)
    def get_interest_rates(self, currency):
        """
        Get interest rates for a currency
        """

        return self.api_request('GET', 'ir_ladders/{}'.format(currency))

    # Orders (Authenticated API)
    def buy_limit(self, product_id, quantity, price):
        """
        # Buy limit order
        """
        params = {
            'order_type': 'limit',
            'product_id': product_id,
            'side': 'buy',
            'quantity': quantity,
            'price': price
        }

        return self.api_request('POST', 'orders', {'order': params})

    def sell_limit(self, product_id, quantity, price):
        """
        Sell limit order
        """
        params = {
            'order_type': 'limit',
            'product_id': product_id,
            'side': 'sell',
            'quantity': quantity,
            'price': price
        }

        return self.api_request('POST', 'orders', {'order': params})

    def buy_market(self, product_id, quantity, price):
        """
        Buy market order
        """
        params = {
            'order_type': 'market',
            'product_id': product_id,
            'side': 'buy',
            'quantity': quantity,
            'price': price
        }

        return self.api_request('POST', 'orders', {'order': params})

    def sell_market(self, product_id, quantity, price):
        """
        Sell market order
        """
        params = {
            'order_type': 'market',
            'product_id': product_id,
            'side': 'sell',
            'quantity': quantity,
            'price': price
        }

        return self.api_request('POST', 'orders', {'order': params})

    def get_order(self, order_id, funding_currency=None, product_id=None,
                  status=None, with_details=False):
        """
        Get order details
        """
        params = {}
        if funding_currency is not None:
            params['funding_currency'] = funding_currency
        if product_id is not None:
            params['product_id'] = product_id
        if status is not None:
            params['status'] = status
        if with_details is not False:
            params['with_details'] = 1

        return self.api_request('GET', 'orders/{}'.format(order_id), params)

    def cancel_order(self, order_id):
        """
        Cancel an order
        """

        return self.api_request('PUT', 'orders/{}/cancel'.format(order_id))

    def edit_order(self, order_id, quantity, price):
        """
        Edit a live order
        """
        params = {
            'quantitiy': quantity,
            'price': price
        }

        return self.api_request('PUT', 'orders/{}'.format(order_id),
                                {'order': params})

    def get_order_trades(self, order_id):
        """
        Get order trades
        """

        return self.api_request('GET', 'orders/{}/trades'.format(order_id))

    def get_order_executions(self, order_id, limit=None, page=None):
        """
        Get order executions
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if page is not None:
            params['page'] = page

        return self.api_request('GET', 'orders/{}/executions'.format(order_id),
                                params)

    # Executions (Authenticated API)
    def get_own_executions(self, product_id):
        """
        Get your executions
        """
        params = {
            'product_id': product_id
        }

        return self.api_request('GET', 'executions/me', params)

    # Accounts (Authenticated API)
    def get_fiat_accounts(self):
        """
        Get fiat accounts
        """

        return self.api_request('GET', 'fiat_accounts')

    def create_fiat_account(self, currency):
        """
        Create fiat account
        """
        params = {
            'currency': currency
        }
        return self.api_request('POST', 'fiat_accounts', params)

    def get_crypto_accounts(self):
        """
        Get fiat accounts
        """

        return self.api_request('GET', 'crypto_accounts')

    def get_accounts(self):
        """
        Get all accounts
        """

        return self.api_request('GET', 'accounts/balance')

    # Assets Lending (Authenticated API)
    def create_loan_bids(self, rate, quantity, currency):
        """
        Create loan bids
        """
        params = {
            'rate': rate,
            'quantity': quantity,
            'currency': currency
        }

        return self.api_request('POST', 'loan_bids', {'loan_bid': params})

    def get_loan_bids(self, currency=None):
        """
        Get loan bids
        """
        params = {}
        if currency is not None:
            params['currency'] = currency

        return self.api_request('GET', 'loan_bids', params)

    def close_loan_bid(self, loan_id):
        """
        Close loan bid
        """

        return self.api_request('PUT', 'loan_bids/{}/close'.format(loan_id))

    def get_loan(self, currency):
        """
        Get loans
        """
        params = {
            'currency': currency
        }

        return self.api_request('GET', 'loans', params)

    def update_loan(self, loan_id, fund_reloaned):
        """
        Update a loan
        """
        params = {
            'fund_reloaned': fund_reloaned
        }

        return self.api_request('PUT', 'loan/{}'.format(loan_id),
                                {'loan': params})

    # Trading Accounts (Authenticated API)
    def get_trading_accounts(self):
        """
        Get trading accounts
        """

        return self.api_request('GET', 'trading_accounts')

    def get_trading_account(self, account_id):
        """
        Get trading account
        """

        return self.api_request('GET', 'trading_accounts/{}'.format(
                                account_id))

    def update_leverage_level(self, account_id, leverage_level):
        """
        Update leverage level
        """
        params = {
            'leverage_level': leverage_level
        }

        return self.api_request('PUT', 'trading_accounts/{}'.format(
                                account_id), {'trading_account': params})

    # Trades (Authenticated API)
    def get_trades(self, funding_currency=None, status=None):
        """
        Get trading accounts
        """
        params = {}
        if funding_currency is not None:
            params['funding_currency'] = funding_currency
        if status is not None:
            params['status'] = status

        return self.api_request('GET', 'trading_accounts', params)

    def close_trade(self, trade_id, closed_quantity=None):
        """
        Close a trade
        """
        params = {}
        if closed_quantity is not None:
            params['closed_quantity'] = closed_quantity

        return self.api_request('PUT', 'trades/{}/close'.format(trade_id),
                                params)

    def close_trades(self, side=None):
        """
        Close a trade
        """
        params = {}
        if side is not None:
            params['side'] = side

        return self.api_request('PUT', 'trades/close_all', params)

    def update_trade(self, trade_id, stop_loss, take_profit):
        """
        Update a trade
        """
        params = {
            'stop_loss': stop_loss,
            'take_profit': take_profit
        }

        return self.api_request('PUT', 'trades/{}'.format(trade_id),
                                {'trade': params})

    def get_trade_loan(self, trade_id):
        """
        Get trade's loan
        """

        return self.api_request('GET', 'trades/{}/loans'.format(trade_id))
