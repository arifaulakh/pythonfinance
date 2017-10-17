from coinbase.wallet.client import Client

client = Client(api_key = '5cP3Cov8sOJROEjt', api_secret = 'PUyjLtVwB7JGjSFu2tz4M9XQxzoP4Ryt', api_version='2017-09-16')
# Get your primary coinbase account
primary_account = client.get_primary_account()

tx = primary_account.send_money(to='bhuri@utschools.ca',
                                amount='0.00001',
                                currency='BTC')
print(tx)
