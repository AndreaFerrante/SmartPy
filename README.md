***
Before proceding, make sure to have all the necessary packages in place:

1. **python -m pip install web3** (interact with the blockchain in Python)
2. **python -m pip install python-dotenv** (to read key-value pairs from)
3. **python -m pip install py-solc-x** (compile solidity smart contracts in Python)
4. **python -m pip install eth-utils** (functions to interact with Ethereum)

For more about the Solidity Programming Language check: https://docs.soliditylang.org
***

*This is a dummy project to test Python Web3 interaction with Ganache and Infura*

At the same time, the Solidity Contracts present inside the contracts folder could be deployed on Infura or on Alchemy.
To find out the different ***chain_id*** values, please have a look here:

https://chainlist.org/

To build and then deploy on a public *blockchain* please follow these steps:

1. find out the *chain_id* here https://chainlist.org/
2. open a Metamask account here https://metamask.io/
3. open your Metamask newly created wallet and copy its address to "my_address" variable inside "smartpy.py" code
4. sign up on Infura (https://infura.io) and create a new project
5. given the new project in Infura, select "API Keys" and 

Overall, the most *important* things to remember are:

**I)** "bytecode" is the machine information  our Solidity code gets “translated” into
**II)** Application Binary Interface (i.e. ABI): it defines the methods and variables available in a smart contract that we can use to interact wit. "Since smart contracts are converted into bytecode before they get deployed to the blockchain, we need a way to know what operations and interactions we can initiate with them, and we need a standardized way to express those interfaces so that any programming language can be used to interact with smart contracts"
