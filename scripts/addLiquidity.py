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
    "0x55cfDcDd6766CDd58b9945C1A2933b4c38518dd7",  # cUSD
    "0xf0f4DF0cDE2C8cB8660ed022d7a22488F723e702"  # cEUR
]

SWAP_ADDRESS = "0xa95B3abe4834b7310a0F12f67c35F73dbDc53a87"


def main():
    network.gas_limit(8000000)
    admin = accounts.load('dev-1')
    
    swap = Swap.at(SWAP_ADDRESS)
    coins = [ERC20Mock.at(address) for address in COINS]


    print("Deployed at:")
    print("Swap:", swap.address)
    
    for coin in coins:
        coin.approve(swap.address, "100000000000000000000000", {"from": admin})
    
    swap.addLiquidity(['100000000000000000000000', '100000000000000000000000'], '0', '1000000000000000000000000000000000000', {'from': admin})
    

    with open("swap.json", "w") as f:
        json.dump(swap.abi, f)

    return swap
