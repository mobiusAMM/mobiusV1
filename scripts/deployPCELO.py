from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    Swap,
)
from brownie import interface, network
import json


COINS = [
    "0x471EcE3750Da237f93B8E339c536989b8978a438",  # CELO
    "0xE74AbF23E1Fdf7ACbec2F3a30a772eF77f1601E1"  # pCELO
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    swap = Swap.deploy(
        coins,
        [18, 18],
        "Mobius CELO/pCELO LP", 
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
