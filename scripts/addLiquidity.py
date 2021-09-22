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
    "0xd629eb00deced2a080b7ec630ef6ac117e614f1b",  # BTC
    "0xBe50a3013A1c94768A1ABb78c3cB79AB28fc1aCE"  # WBTC
]

SWAP_ADDRESS = "0xA5037661989789d0310aC2B796fa78F1B01F195D"

LP = "0x8cD0E2F11ed2E896a8307280dEEEE15B27e46BbE"

lpAmount = 0.085338250711358822 * 10 ** 18


def main():
    network.gas_limit(8000000)
    # admin = accounts.load('kyle_personal')
    
    swap = Swap.at(SWAP_ADDRESS)
    print(swap.getAdminBalance(0), swap.getAdminBalance(1))
    