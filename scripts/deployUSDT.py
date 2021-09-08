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
    "0x765de816845861e75a25fca122bb6898b8b1282a",  # cUSD
    "0xcFFfE0c89a779c09Df3DF5624f54cDf7EF5fDd5D"  # cUSDT
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

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
        "Mobius cUSD/cUSDT LP", 
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
