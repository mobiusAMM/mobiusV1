from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    Swap,
)
from brownie import interface, network
import json


COINS = [
    "0x765DE816845861e75A25fCA122bb6898B8B1282a",  # cUSD
    "0xB4aa2986622249B1F45eb93F28Cfca2b2606d809"  # pUSD
]


def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')

    coins = [interface.ERC20(addr) for addr in COINS]

    swap = Swap.deploy(
        coins,
        [18, 18],
        "Mobius cUSD/pUSD LP", 
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
