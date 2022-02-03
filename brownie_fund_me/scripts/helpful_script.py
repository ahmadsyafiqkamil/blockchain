from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMAL = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print(f"deploying mock")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, Web3.toWei(STARTING_PRICE, "ether"), {'from': get_account()})
        print("mock deployed")
