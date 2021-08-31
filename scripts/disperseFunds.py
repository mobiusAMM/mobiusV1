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
    "0x2AaF20d89277BF024F463749045964D7e7d3A774",  # cUSD
    "0x3551d53C9CF91E222D9579A1Ac4B44117E8Ec609",
    "0x7588110A070987ea0347Cf788226c28d1476d641",
    "0x17Ec8dab839a9880D656c3cEF40cf4038657d168",
    "0xCC531BfBA46cA251D3D9f3aCc37ABD5DCF3ed0B3"
]

recipient = "0xE35E97438Fd16593e285546260C8585dea7909Dd"


def main():
    network.gas_limit(8000000)
    admin = accounts.load('dev-1')
    
    coins = [ERC20Mock.at(address) for address in COINS]
    
    for coin in coins:
        coin.mint_for_testing(recipient, "100000000000000000000000000", {"from": admin})
    
    