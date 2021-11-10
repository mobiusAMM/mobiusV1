from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    Swap,
)
from brownie import interface, network
import json


COINS = [
    "0xD8763CBa276a3738E6DE85b4b3bF5FDed6D6cA73",  # cEUR
    "0x56072D4832642dB29225dA12d6Fd1290E4744682"  # pEUR
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    swap = Swap.deploy(
        coins,
        [18, 18],
        "Mobius cUER/pEUR LP", 
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
