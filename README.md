# Switch
Lightswitch project for Choice Coin using Algorand Smart Contracts.

Lightswitch takes in one Choice and switches it for two Choice.

1. Sender sends 1 Choice to Application ID ##########.
2. Smart Contract recieves 1 Choice, user address, and smart signature.
3. Smart Contract verifies and approves or rejects data recieved.
4. If the smart contract approves the trransaction, 2 Choice are returned.
5. If the smart contract rejects the transaction, no Choice are returned.


[v0.1 | App ID 2267436284](https://allo.info/application/2267436284)

[v0.1 | App ID 2267616358](https://allo.info/application/2267616358)

```
goal app create --creator 5AL546QOEXTJD3JDO7RIUVTNVCQWNXSRMAULCR7DZYFAIYZP2GWEOKI2PE --approval-prog approval.teal --clear-prog clear_state.teal --global-byteslices 0 --global-ints 0 --local-byteslices 0 --local-ints 0
```
