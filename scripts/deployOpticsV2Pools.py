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

# (name, address, decimals)
COINS = [
    [("cUSD", "0x765de816845861e75a25fca122bb6898b8b1282a", 18),
    ("USDC", "0xef4229c8c3250C675F21BCefa42f58EfbfF6002a", 6)],
    [("cETH", "0x2DEf4285787d58a2f811AF24755A8150622f4361", 18),
     ("wETH", "0x122013fd7dF1C6F636a5bb8f03108E876548b455", 18)],
    [("cBTC", "0xD629eb00dEced2a080B7EC630eF6aC117e614f1b", 18),
     ("wBTC", "0xBAAB46E28388d2779e6E31Fd00cF0e5Ad95E327B", 8)],
    [("cUSD", "0x765de816845861e75a25fca122bb6898b8b1282a", 18),
     ("pUSDC", "0x1bfc26cE035c368503fAE319Cc2596716428ca44", 6)],
    [("cUSD", "0x765de816845861e75a25fca122bb6898b8b1282a", 18),
     ("DAI", "0x90Ca507a5D4458a4C6C6249d186b6dCb02a5BCCd", 18)]
]


def deployPool(tokens, decimals, tokenNames, admin):
    #coins = [interface.ERC20(addr) for addr in tokens]

    MathUtils.deploy({"from": admin})
    SwapUtils.deploy({"from": admin})

    swap = Swap.deploy(
        tokens,
        decimals,
        f'Mobius {"/".join(tokenNames)} LP', 
        "MobLP", 
        50, 
        2 * (10 ** 7), # .2% swap fee
        5 * 10 ** 9, # 50% admin fee
        0,
        0,
        admin.address, 
        {"from": admin},
    )
    print(f'Deployed {"/".join(tokenNames)} pool at {swap.address}')
    print(f'LP Token Address: {swap.getLpToken()}')
    print("-" * 20)
    with open("OpticsV2Deploys.csv", 'a') as fp:
        fp.write(f'{",".join(tokens)},{swap.address},{swap.getLpToken()}' + "\n")


def main():
    network.gas_limit(8000000)
    admin = accounts.load('dev-1')

    for pair in COINS:
        names = [x[0] for x in pair]
        tokens = [x[1] for x in pair]
        decimals = [x[2] for x in pair]
        deployPool(tokens, decimals, names, admin)
