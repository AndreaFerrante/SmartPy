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


# Read the hello_world.sol smart contract ...
smart_contract_helloworld = read_file( './contracts/helloworld.sol' )


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


# Once the smart contract is compiled and saved as a JSON, we must read the ABI and the ByteCode.

# --> get the ABI (first get the JSON, then the real ABI value in it)...
application_binary_interface = json.loads( compiled_smart["contracts"]\
                                                         ["helloworld.sol"]\
                                                         ["HelloWorld"]\
                                                         ["metadata"] )
application_binary_interface = application_binary_interface["output"]["abi"]

# --> get the byte code...
bytecode                     = compiled_smart["contracts"]\
                                             ["helloworld.sol"]\
                                             ["HelloWorld"]\
                                             ["evm"]\
                                             ["bytecode"]\
                                             ["object"]





