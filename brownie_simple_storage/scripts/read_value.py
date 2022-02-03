from brownie import simpleStorage, accounts, config

def read_contract():
    # print(simpleStorage[-1])
    ss = simpleStorage[-1]
    print(ss.retrive())

def main():
    read_contract()