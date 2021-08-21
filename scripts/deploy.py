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


def main():
    admin = accounts.load('mob')

    if COINS:
        coins = [interface.ERC20(addr) for addr in COINS]
    else:
        coins = [
            ERC20Mock.deploy(name, name, 18, {"from": accounts[0]}) for name in ["cUSD", "cEUR"]
        ]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        coins,
        [18, 18],
        "Mobius LP", 
        "MobLP", 
        1500, 
        .001, 
        0, 
        0,
        0,
        accounts[0], 
        {"from": admin},
    )

    print("Deployed at:")
    print("Swap:", swap.address)

    with open("swap.json", "w") as f:
        json.dump(swap.abi, f)

    return swap
