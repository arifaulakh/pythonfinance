from coinbase.wallet.client import Client

client = Client(api_key = '5cP3Cov8sOJROEjt', api_secret = 'PUyjLtVwB7JGjSFu2tz4M9XQxzoP4Ryt', api_version='2017-09-16')

currency_code = 'CAD'  # can also use EUR, CAD, etc.

# Make the request
price = client.get_spot_price(currency=currency_code)

print (price)





