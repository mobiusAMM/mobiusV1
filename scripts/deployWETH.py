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
    "0x2def4285787d58a2f811af24755a8150622f4361",  # cETH
    "0xE919F65739c26a42616b7b8eedC6b5524d1e3aC4"  # WETH
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        coins,
        [18, 18],
        "Mobius cETH/WETH LP", 
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
