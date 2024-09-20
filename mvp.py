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
        Gtxn[1].type_enum() == TxnType.Payment,                         
        Gtxn[1].amount() >= funding_amount,                             
        Gtxn[1].receiver() == Global.current_application_address()     
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
    user_specified_amount = Int(100) 
    is_valid_transfer = And(
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].xfer_asset() == asset_id,
        Gtxn[1].asset_receiver() == Global.current_application_address(),
        Gtxn[1].asset_amount() == user_specified_amount 
    )
    # return transaction to user
    ############################
    send_to_user = Seq([
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.AssetTransfer,
            TxnField.xfer_asset: asset_id,
            TxnField.asset_receiver: Txn.sender(),  
            TxnField.asset_amount:  Mul(user_specified_amount, Int(2)),  
        }),
        InnerTxnBuilder.Submit(),
        Approve()  
    ])

    ##############################
    # Return Condition
    ##############################
    return Cond(
        [Txn.application_id() == Int(0), on_create],           
        [is_opt_in, Approve()], 
        [is_funding_txn, escrow_opt_in],                             
        [is_valid_transfer, send_to_user],             
        [Int(1), Reject()]                                   
    )
    ##############################

# Compile Teal Approval Program
if __name__ == "__main__":
    print(compileTeal(approval_program(), mode=Mode.Application, version=10))
