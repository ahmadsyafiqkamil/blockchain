from scripts.helpful_script import get_account, get_contract
from brownie import Lottery, config, network


def deploy_lottery():
    account = get_account(id="syafiq-project-account")
    Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("eth_usd_price_feed").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery!")
    return


def main():
    deploy_lottery()
