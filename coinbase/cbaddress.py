from coinbase.wallet.client import Client

client = Client(api_key = '5cP3Cov8sOJROEjt', api_secret = 'PUyjLtVwB7JGjSFu2tz4M9XQxzoP4Ryt', api_version='2017-09-16')

# Get your primary coinbase account
primary_account = client.get_primary_account()
address = primary_account.create_address()
print(address)