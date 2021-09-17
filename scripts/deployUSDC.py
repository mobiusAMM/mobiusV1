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
    "0x765de816845861e75a25fca122bb6898b8b1282a", # cUSD
    "0x2A3684e9Dc20B857375EA04235F2F7edBe818FA7", # USDC
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        coins,
        [18, 6],
        "Mobius cUSD/USDC LP", 
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
