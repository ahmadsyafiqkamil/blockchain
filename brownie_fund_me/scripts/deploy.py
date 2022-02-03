from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN
)


def deploy_fund_me():
    account = get_account()
    # pass priceFeed
    # address or mock adress

    if network.show_active() not in LOCAL_BLOCKCHAIN:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"contract deploy {fundme.address}")


def main():
    deploy_fund_me()
