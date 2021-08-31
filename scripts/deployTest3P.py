import requests
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    LPToken,
    Swap,
    ERC20Mock,
    compile_source,
    SwapUtils, 
    MathUtils
)
from brownie import interface, network
import json


COINS = [
    # "0x765de816845861e75a25fca122bb6898b8b1282a",  # cUSD
    # "0xd8763cba276a3738e6de85b4b3bf5fded6d6ca73"  # cEUR
]

TEST_ACCOUNTS = ["0x42F21354603C7f4065C40C80c88fA8d0Db4d4EA9",
                 "0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9",
                 "0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850",
                 "0xCD943EE26221AC3e6e7f3e38598F2b08BAEA87DD",
                 "0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850"]

def main():
    network.gas_limit(8000000)
    admin = accounts.load('dev-1')

    
    coins = [
        ERC20Mock.deploy(name, name, 18, TEST_ACCOUNTS, {"from": accounts[0]}) for name in ["TC3", "TC4", 'TC5']
    ]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        coins,
        [18, 18, 18],
        "Mobius LP", 
        "MobLP", 
        1500, 
        .002, 
        .001, 
        0,
        0,
        accounts[0], 
        {"from": admin},
    )

    print("Deployed at:")
    print("Swap:", swap.address)
    
    for coin in coins:
        coin.approve(swap.address, "100000000000000000", {"from": admin})
    
    swap.addLiquidity(['100000000000000000', '100000000000000000', "100000000000000000"], '0', '1000000000000000000000000000000000000', {'from': admin})
    

    with open("swap.json", "w") as f:
        json.dump(swap.abi, f)

    return swap
