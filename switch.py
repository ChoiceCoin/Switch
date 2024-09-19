##############################
# import everything from pyteal
from pyteal import *
##############################

##############################
# Function for generating approval program
def approval_program():
    ##############################

    ##############################
    # Asset ID
    asset_id = Int(297995609)
    # Create app
    on_create = Approve()
    # Allow optin
    is_opt_in = Txn.on_completion() == OnComplete.OptIn
    ##############################

    ############################################################
    # Optin Logic
    ############################################################
    # Detect the funding transaction (1 Algo sent to the escrow)
    ##############################
    funding_amount = Int(1000000)  
    is_funding_txn = And(
        Txn.type_enum() == TxnType.Payment,                         
        Txn.amount() >= funding_amount,                             
        Txn.receiver() == Global.current_application_address()     
    )
    ##############################
    # Logic for opt-in to the asset_id using an inner transaction
    ##############################
    escrow_opt_in = Seq([
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.AssetTransfer,
            TxnField.xfer_asset: asset_id,
            TxnField.asset_receiver: Global.current_application_address(),  
            TxnField.asset_amount: Int(0),  
        }),
        InnerTxnBuilder.Submit(),
        Approve()  
    ])
    ##############################
    
    ############################################################
    # App logic
    ############################################################
    # User specified amount
    user_specified_amount = Btoi(Txn.application_args[0])
    is_valid_transfer = And(
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == asset_id,
        Txn.asset_receiver() == Global.current_application_address(),
        Txn.asset_amount() == user_specified_amount 
    )
    ##############################
    # Generate random number
    ##############################
    round_number = Global.round()
    time_stamp = Global.latest_timestamp()
    combined = Sha256(Concat(Itob(round_number), Itob(time_stamp)))  
    normalized_random_value = Btoi(combined) % Int(2) 
    ############################
    # return transaction to user
    ############################
    send_to_user = InnerTxnBuilder.Execute({
        TxnField.type_enum: TxnType.AssetTransfer,
        TxnField.xfer_asset: asset_id,
        TxnField.asset_amount: Mul(user_specified_amount, Int(2)), 
        TxnField.asset_receiver: Txn.sender(),
    })
    ##############################
    # return transaction to burn address
    ##############################
    send_to_burn = InnerTxnBuilder.Execute({
        TxnField.type_enum: TxnType.AssetTransfer,
        TxnField.xfer_asset: asset_id,
        TxnField.asset_amount: user_specified_amount,  
        TxnField.asset_receiver: Addr("6G5V4U2MCW5TIZ7JP6BZFQELTGGJBEG5EVSQRQQRLEZM3V6DXOPV5TUJQA"),
    })
    ##############################
    # conditional logic and execution
    ##############################
    handle_random_txn = If(
        normalized_random_value == Int(1),
        Seq([send_to_user, Approve()]),  
        Seq([send_to_burn, Approve()])  
    )
    ##############################

    ##############################
    # Return Condition
    ##############################
    return Cond(
        [Txn.application_id() == Int(0), on_create],           
        [is_opt_in, Approve()], 
        [is_funding_txn, escrow_opt_in],                             
        [is_valid_transfer, handle_random_txn],             
        [Int(1), Reject()]                                   
    )
    ##############################

# Compile Teal Approval Program
if __name__ == "__main__":
    print(compileTeal(approval_program(), mode=Mode.Application, version=10))
