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

SWAP_ADDRESS = "0x19260b9b573569dDB105780176547875fE9fedA3"

LP = "0x8cD0E2F11ed2E896a8307280dEEEE15B27e46BbE"

lpAmount = 0.085338250711358822 * 10 ** 18


def main():
    network.gas_limit(8000000)
    # admin = accounts.load('kyle_personal')
    add = "0xf773C3F00F119985e98cfdF33BB20dcb778fe677"
    
    swap = Swap.at(SWAP_ADDRESS)
    coins = [interface.ERC20(addr) for addr in COINS]
    lp = LPToken.at(LP)
    print(lp)
    
    # for coin in coins:
    #     coin.approve(swap.address, .05 * 10 ** 18, {"from": admin})
    # lp.approve(swap.address, lpAmount, {"from": admin})
    
    # swap.removeLiquidity(lpAmount, [.047* 10 ** 18, .047 * 10 ** 8], '1000000000000000000000000000000000000', {'from': admin})
    print(swap.getBalances())
    print(lp.balanceOf(add))
    print(swap.calculateRemoveLiquidity(add, lp.balanceOf(add)))
    # swap.addLiquidity([.05 * 10 ** 16, .05 * 10 ** 6], 0, '1000000000000000000000000000000000000', {'from': admin})
    