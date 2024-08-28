from pyteal import *

def approval_program():
    # Constants
    asset_id = Int(297995609)
    receiver_address = Addr("5AL546QOEXTJD3JDO7RIUVTNVCQWNXSRMAULCR7DZYFAIYZP2GWEOKI2PE")

    # Log the type of transaction
    log_type = Log(Bytes("Txn Type"))
    
    # Log the XferAsset
    log_asset_id = Log(Itob(Txn.xfer_asset()))
    
    # Log the AssetAmount
    log_asset_amount = Log(Itob(Txn.asset_amount()))

    # Create app logic
    on_create = Seq([
        Approve()
    ])

    # Conditions for normal operation
    is_axfer = Txn.type_enum() == TxnType.AssetTransfer
    correct_asset_id = Txn.xfer_asset() == asset_id
    correct_asset_amount = Txn.asset_amount() == Int(1)
    correct_receiver = Txn.receiver() == receiver_address
    conditions_met = And(is_axfer, correct_asset_id, correct_asset_amount, correct_receiver)

    # Logic to send 2 CHOICE tokens back to the sender
    send_two_choice = Seq([
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetField(TxnField.type_enum, TxnType.AssetTransfer),
        InnerTxnBuilder.SetField(TxnField.xfer_asset, asset_id),
        InnerTxnBuilder.SetField(TxnField.asset_amount, Int(2)),
        InnerTxnBuilder.SetField(TxnField.receiver, Txn.sender()),
        InnerTxnBuilder.Submit(),
        Approve()
    ])

    # Main approval program logic with logs
    program = Cond(
        # Handle app creation
        [Txn.application_id() == Int(0), on_create],
        
        # Log and check conditions
        [is_axfer, Seq([log_type, Approve()])],
        [correct_asset_id, Seq([log_asset_id, Approve()])],
        [correct_asset_amount, Seq([log_asset_amount, Approve()])],
        
        # Handle normal asset transfer
        [conditions_met, send_two_choice],
        
        # Reject if no conditions are met
        [Int(1), Reject()]
    )
    
    return program

def clear_state_program():
    return Approve()

# Compile the PyTeal to TEAL
if __name__ == "__main__":
    # Set version to 5, which is required for inner transactions
    approval_teal = compileTeal(approval_program(), mode=Mode.Application, version=5)
    clear_teal = compileTeal(clear_state_program(), mode=Mode.Application, version=5)

    print("Approval Program:")
    print(approval_teal)
    
    print("\nClear State Program:")
    print(clear_teal)
