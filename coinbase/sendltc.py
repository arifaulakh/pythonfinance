from coinbase.wallet.client import Client

client = Client(api_key = '#', api_secret = '#', api_version='2017-09-16')
# Get your primary coinbase account
primary_account = client.get_primary_account()

tx = primary_account.send_money(to='#',
                                amount='0.00001',
                                currency='BTC')
print(tx)
