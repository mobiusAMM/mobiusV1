from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    Swap,
    ERC20Mock,
    SwapUtils, 
    MathUtils
)
from brownie import interface, network
import json


COINS = [
    "0xd629eb00deced2a080b7ec630ef6ac117e614f1b",  # BTC
    "0xBe50a3013A1c94768A1ABb78c3cB79AB28fc1aCE"  # WBTC
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        coins,
        [18, 8],
        "Mobius BTC/WBTC LP", 
        "MobLP", 
        50, 
        10 ** 7, # .1% swap fee
        10 ** 9, # 10% admin fee
        0,
        0,
        admin.address, 
        {"from": admin},
    )

    print("Deployed at:")
    print("Swap:", swap.address)

    with open("swap.json", "w") as f:
        json.dump(swap.abi, f)

    return swap
