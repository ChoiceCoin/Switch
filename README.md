# Lightswitch

Lightswitch project for Choice Coin using Algorand Smart Contracts.


# Versions

For complete versions history, see versions.md. Version **v1.0** and **v1.1** are functional.

____________________________________________________________
**v1.0**
____________________________________________________________
Lightswitch **v1.0** takes in one Choice and switches it for two Choice.

1. Sender sends 1 Choice to Application ID ##########.
2. Smart Contract recieves 1 Choice, user address, and smart signature.
3. Smart Contract verifies and approves or rejects data recieved.
4. If the smart contract approves the trransaction, 2 Choice are returned.
5. If the smart contract rejects the transaction, no Choice are returned.

v1.0 App ID 2307526839 | [PeraExplorer](https://explorer.perawallet.app/application/2307526839/) | [AlloExplorer](https://allo.info/application/2307526839)

v1.0 App Account W4G35ELHNB5L34MD72WV2TM4HE54NM7TRJKXZCFUMBHXVQOWGBVUB2I5W4 | [PeraExplorer](https://explorer.perawallet.app/address/W4G35ELHNB5L34MD72WV2TM4HE54NM7TRJKXZCFUMBHXVQOWGBVUB2I5W4/) | [AlloExplorer](https://allo.info/account/W4G35ELHNB5L34MD72WV2TM4HE54NM7TRJKXZCFUMBHXVQOWGBVUB2I5W4)

____________________________________________________________
**v1.1**
____________________________________________________________
Lightswitch **v1.0**  has an Application ID and an escrow account.

The smart contract:
1. Is fundable with Choice and Algo.
2. Allows users to optin to the Application ID.
3. Recieves transactions from users.
4. Validates the transaction from the user.
5. Deploys conditional logic based on the validation.
6. If the validation is 1, the contract sends the user 2x the amount of Choice sent.
7. If the validation is 0, the contract does nothing.

v1.1 App ID 2311621083 | [PeraExplorer](https://explorer.perawallet.app/application/2311621083/) | [AlloExplorer](https://allo.info/application/2311621083)

v1.1 App Account KMJG6OAMMSQYEQPEEQ3V5VZVPLEE3FLGIIRBGTOQMINOFKONGGOH6BCOHE | [PeraExplorer](https://explorer.perawallet.app/address/KMJG6OAMMSQYEQPEEQ3V5VZVPLEE3FLGIIRBGTOQMINOFKONGGOH6BCOHE/) | [AlloExplorer](https://allo.info/account/KMJG6OAMMSQYEQPEEQ3V5VZVPLEE3FLGIIRBGTOQMINOFKONGGOH6BCOHE)
____________________________________________________________

Command line instructions for deployment.

```
goal app create --creator 5AL546QOEXTJD3JDO7RIUVTNVCQWNXSRMAULCR7DZYFAIYZP2GWEOKI2PE --approval-prog approval.teal --clear-prog clear_state.teal --global-byteslices 0 --global-ints 0 --local-byteslices 0 --local-ints 0
```
____________________________________________________________

____________________________________________________________
# References
____________________________________________________________
[Build an Algorand Smart Contract](https://github.com/Bhaney44/Build-an-Algorand-Smart-Contract)

[PyTeal](https://pyteal.readthedocs.io/en/stable/)

[The Algorand Virtual Machine and TEAL](https://developer.algorand.org/docs/get-details/dapps/avm/teal/specification/)

[Algorand v10 opcodes](https://developer.algorand.org/docs/get-details/dapps/avm/teal/opcodes/v10/)


