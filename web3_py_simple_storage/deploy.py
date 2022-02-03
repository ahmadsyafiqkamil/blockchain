import json
import os

from solcx import compile_standard
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

compile = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metada ta", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.8.7"
)

with open("compiled_code.json", "w") as file:
    json.dump(compile, file)

bytecode = compile["contracts"]["SimpleStorage.sol"]["simpleStorage"]["evm"]["bytecode"]["object"]
abi = compile["contracts"]["SimpleStorage.sol"]["simpleStorage"]["abi"]
# print(bytecode)
# print(abi)

# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/003407eef50141a2af1c6b8b39ec0b2c"))
# chain_id = 1337
chain_id = 4
address = "0x7ea3C3B6C545C758446D3f93D308a6940Fcf1ebC"
private_key = os.getenv("PRIVATE_KEY")
# print(private_key)

# create contract
simple_storage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(simple_storage)
# latest transaction
nonce = w3.eth.getTransactionCount(address)
# print(nonce)
# 1. build a transaction
# 2. sign a transaction
# 3. send a transaction
transaction = simple_storage.constructor().buildTransaction({"chainId": chain_id, "from": address, "nonce": nonce})
# print(transaction)
sign_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(sign_tx)
tx_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
# print(tx_hash)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

"""
working with contract, you need:
Contract ABI
Contract Address
"""

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
"""
call -> simulate making the call and getting return value
transact -> actually make a state change
"""
# print(simple_storage.functions.retrive().call())
# print(simple_storage.functions.store(15).call())
print(simple_storage.functions.retrive().call())
store_transaction = simple_storage.functions.store(15).buildTransaction({
    "chainId": chain_id, "from": address, "nonce": nonce + 1
})
sign_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
send_store_tx = w3.eth.sendRawTransaction(sign_store_tx.rawTransaction)
send_store_receipt = w3.eth.waitForTransactionReceipt(send_store_tx)
print(simple_storage.functions.retrive().call()) 
