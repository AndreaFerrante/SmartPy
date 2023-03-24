'''
Before proceding, make sure to have all the necessary packages in place:

1. python -m pip install web3          --> interact with the blockchain in Python
2. python -m pip install python-dotenv --> to read key-value pairs from
3. python -m pip install py-solc-x     --> compile solidity smart contracts in Python
4. python -m pip install eth-utils     --> functions to interact with Ethereum

For more about the Solidity Programming Language check: https://docs.soliditylang.org

'''


import json
# Import all needed packages ...
import os
from web3 import Web3
from smartpy.utils import *
from eth_utils import address
from dotenv import load_dotenv
from solcx import compile_standard, install_solc


########################################################################################################################
# Read the hello_world.sol smart contract ...
smart_contract_helloworld = read_file( './contracts/helloworld.sol' )


########################################################################################################################
# After that the content is read, compile in Python the contract to obtain:
#
# 1. ABI:
# 2. ByteCode:
#
# Important that the version of Solidity used is the same of the one used in the smart contract !


sol_version = "0.8.13"
install_solc(sol_version)

compiled_smart = compile_standard(

    {
        "language": "Solidity",
        "sources":  {"helloworld.sol":   {"content": smart_contract_helloworld}},
        "settings": {"outputSelection":  {
                                            "*": {
                                                  "*": ["abi",
                                                        "metadata",
                                                        "evm.bytecode",
                                                        "evm.bytecode.sourceMap"]
                                                 }
                                         }
                     },
    },
    solc_version="0.8.13"

)

write_compiled_file_to_json(file_to_save     = compiled_smart,
                            path_filename    = './build/compiled_smart')


########################################################################################################################
# Once the smart contract is compiled and saved as a JSON, we must read the ABI and the ByteCode.

# --> get the ABI (first get the JSON, then the real ABI value in it)...
application_binary_interface = json.loads( compiled_smart["contracts"]\
                                                         ["helloworld.sol"]\
                                                         ["HelloWorld"]\
                                                         ["metadata"] )
application_binary_interface = application_binary_interface["output"]["abi"]

# --> get the byte code...
byte_code                    = compiled_smart["contracts"]\
                                             ["helloworld.sol"]\
                                             ["HelloWorld"]\
                                             ["evm"]\
                                             ["bytecode"]\
                                             ["object"]


########################################################################################################################
# Connect to ganache to see the smart contract in action locally...

web_3       = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id    = 1337
my_address  = "0x665884dDa40F02013831f9Db3495E464c709f0C0"
private_key = "0x9369be73e3fbe2541d59d53482efdf8bdf944dce53f67710ff66211c0455b444"


########################################################################################################################
# Now, we are ready to send the contract on Ganache !

hello_world = web_3.eth.contract(abi = application_binary_interface, bytecode = byte_code)
nonce       = web_3.eth.getTransactionCount(my_address)
transaction = hello_world.constructor().buildTransaction({"chainId": chain_id,
                                                          "from":    my_address,
                                                          "nonce":   nonce})
signed      = web_3.eth.account.signTransaction(transaction, private_key=private_key)
hash        = web_3.eth.send_raw_transaction(signed.rawTransaction)
receipt     = web_3.eth.wait_for_transaction_receipt(hash)



########################################################################################################################
# To interact with any blockchain the coder can do 2 things: call and / or transact:
#
# 1. call     ---> functions in the contract that do make state changes
# 2. transact ---> create state changes in the contract

storage_sol         = web_3.eth.contract(abi = application_binary_interface, address = receipt.contractAddress)
call_fun            = storage_sol.functions.sayHelloWorld().buildTransaction( {"chainId": chain_id,
                                                                               "from":    my_address,
                                                                               "nonce":  nonce + 1} )
sign_call_fun       = web_3.eth.account.signTransaction(call_fun, private_key = private_key)
tx_call_fun_hash    = web_3.eth.send_raw_transaction(sign_call_fun.rawTransaction)
tx_call_fun_receipt = web_3.eth.wait_for_transaction_receipt(tx_call_fun_hash)

# -------------------------------------------------
print(storage_sol.functions.sayHelloWorld().call())
# -------------------------------------------------


