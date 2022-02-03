from brownie import accounts, config, simpleStorage, network


def deploy_simple_storage():
    account = get_account()
    ss = simpleStorage.deploy({"from":account})
    stored_value = ss.retrive()
    print(stored_value)
    tx_store = ss.store(15,{"from":account})
    tx_store.wait(1)
    updated_store_value =ss.retrive()
    print(updated_store_value)


    # account = accounts.load("syafiq-project-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
