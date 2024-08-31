from pyteal import *

def approval_program():
    # Simple example conditions
    on_create = Approve()
    is_opt_in = Txn.on_completion() == OnComplete.OptIn
    handle_funding = Txn.amount() > Int(0)  # Funding condition
    is_choice_transfer = Txn.asset_amount() > Int(0)  # CHOICE transfer condition
    handle_user_txn = Approve()  # Example user transaction handling

    return Cond(
        [Txn.application_id() == Int(0), on_create],
        [is_opt_in, Approve()],
        [handle_funding, Approve()],
        [is_choice_transfer, handle_user_txn],
        [Int(1), Reject()]  # Reject any unmatched transactions
    )

if __name__ == "__main__":
    print(compileTeal(approval_program(), mode=Mode.Application, version=5))
