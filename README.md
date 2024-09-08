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

Version v0.0 - v0.4 are live, but not properly functional.

[v0.0 | App ID 2267436284](https://allo.info/application/2267436284)

[v0.1 | App ID 2267616358](https://allo.info/application/2267616358)

[v0.2 | App ID 2267749636](https://allo.info/application/2267749636)

[v0.3 | App ID 2269161869](https://allo.info/application/2269161869)

[v0.4 | App ID 2269165240](https://allo.info/application/2269165240)

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




