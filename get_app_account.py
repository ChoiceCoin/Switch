######################################################################################################################
######################################################################################################################
######################################################################################################################
from algosdk import logic
from algosdk.v2client.algod import AlgodClient
######################################################################################################################
######################################################################################################################
######################################################################################################################
user_mnemonic = "fruit climb pelican vicious absent mesh program alarm siren deliver lawsuit cram upgrade priority elephant claw hero this mandate syrup essay object reject abstract mouse"
user_address = "Q4HNMIAR7DJ6WB6EIR7AX62B2Z4HHD7CA4KISQQ5NM22KIMKKDK54QBRH4"
user_private_key = mnemonic.to_private_key(user_mnemonic)
algod_client = AlgodClient('', 'https://mainnet-api.algonode.cloud', headers={'User-Agent': 'algosdk'})

app_id = 2269165240
app_addr = logic.get_application_address(app_id)

print(f"Application ID:   {app_id}")
print(f"Application Addr: {app_addr}")
