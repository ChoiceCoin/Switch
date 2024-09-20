# Lightswitch

Lightswitch project for Choice Coin using Algorand Smart Contracts.

____________________________________________________________
Lightswitch takes in one Choice and switches it for two Choice.

1. Sender sends 1 Choice to Application ID ##########.
2. Smart Contract recieves 1 Choice, user address, and smart signature.
3. Smart Contract verifies and approves or rejects data recieved.
4. If the smart contract approves the trransaction, 2 Choice are returned.
5. If the smart contract rejects the transaction, no Choice are returned.

____________________________________________________________
# Versions

Version v0.0 - v0.4 are live and use Teal 5, but not properly functional. Version v0.5 and v0.6 both use Teal 10, but are also not functional.
Version v0.7 - v0.9 are able to optin, but not functional as applications.
Version v1.0 is functional.

**v0.0**

[v0.0 App ID 2267436284](https://allo.info/application/2267436284)

**v0.1**

[v0.1 App ID 2267616358](https://allo.info/application/2267616358)

**v0.2**

[v0.2 App ID 2267749636](https://allo.info/application/2267749636)

**v0.3**

[v0.3 App ID 2269161869](https://allo.info/application/2269161869)

**v0.4**

[v0.4 App ID 2269165240](https://allo.info/application/2269165240)

[v0.4 App Account 3IIMGQUYHAGU7RXFTCD6KO5N4TNMWKWY5UIHMNGHNAXWTCCB5G6Z2XH3II](https://allo.info/account/3IIMGQUYHAGU7RXFTCD6KO5N4TNMWKWY5UIHMNGHNAXWTCCB5G6Z2XH3II)

**v0.5**

[v0.5 App ID 2302405696](https://allo.info/application/2302405696)

[v0.5 App Account E57YHA5WQZCEOHJ326R3SACSHK3HRRWBUFTYBH4E2SBYYNIFOVQD7ZDUAQ](https://allo.info/account/E57YHA5WQZCEOHJ326R3SACSHK3HRRWBUFTYBH4E2SBYYNIFOVQD7ZDUAQ)

**v0.6**

[v0.6 App ID 2304378520](https://allo.info/application/2304378520)

[v0.6 App Account FEZCDW5JVYUMGDDMOBDNAUFEQFSG2QM322XKEMG4OPTXLD4PLDCWXVPLG4](https://allo.info/account/FEZCDW5JVYUMGDDMOBDNAUFEQFSG2QM322XKEMG4OPTXLD4PLDCWXVPLG4)

**v0.7**

v0.7 App ID 2307344688

v0.7 App Account B44AKSMBEO6ZVAWSXSQX2AIE3Z5OCMNYZEATNOBBSWEIXZHRMO6YPDE4J4

**v0.8**

v0.8 2307395041

v0.8 4CQG7GKSMFSO427SKDRR2OYE7TKZRA56JXXGMOPH2YJHZ7RYIFGU5RJNSM

**v0.9**

v0.9 2307432714

v0.9 VKOTZ7M53NP56BKDFXOFNCVJDJEORIY7F6WZXOEGKXYJ2YIEQANORKKZS4

**v1.0**

v1.0 [2307526839](https://allo.info/application/2307526839)

v1.0 [W4G35ELHNB5L34MD72WV2TM4HE54NM7TRJKXZCFUMBHXVQOWGBVUB2I5W4](https://allo.info/account/W4G35ELHNB5L34MD72WV2TM4HE54NM7TRJKXZCFUMBHXVQOWGBVUB2I5W4)
____________________________________________________________

Command line instructions.

```
goal app create --creator 5AL546QOEXTJD3JDO7RIUVTNVCQWNXSRMAULCR7DZYFAIYZP2GWEOKI2PE --approval-prog approval.teal --clear-prog clear_state.teal --global-byteslices 0 --global-ints 0 --local-byteslices 0 --local-ints 0
```
____________________________________________________________

# Database functionality

Lightswitch has an Application ID and an escrow account.

The smart contract:
1. Is fundable with Choice and Algo.
2. Allows users to optin to the Application ID.
3. Recieves transactions from users.
4. Validates the transaction from the user.
5. Deploys conditional logic based on the validation.
6. If the validation is 1, the contract sends the user 2x the amount of Choice sent.
7. If the validation is 0, the contract does nothing.


# References

[Build an Algorand Smart Contract](https://github.com/Bhaney44/Build-an-Algorand-Smart-Contract)

[PyTeal](https://pyteal.readthedocs.io/en/stable/)

[The Algorand Virtual Machine and TEAL](https://developer.algorand.org/docs/get-details/dapps/avm/teal/specification/)

[Algorand v10 opcodes](https://developer.algorand.org/docs/get-details/dapps/avm/teal/opcodes/v10/)


