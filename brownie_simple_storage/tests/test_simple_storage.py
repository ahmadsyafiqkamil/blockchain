from brownie import simpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    ss = simpleStorage.deploy({"from": account})
    starting_value = ss.retrive()
    expected = 15
    # assert
    assert starting_value == expected

def test_update():
    # arrange
    account = accounts[0]
    # act
    ss = simpleStorage.deploy({"from": account})
    expected = 15
    ss.store(expected,{"from": account})
    # assert
    assert expected == ss.retrive()