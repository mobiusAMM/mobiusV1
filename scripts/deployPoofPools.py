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
    ("pUSD", "0xB4aa2986622249B1F45eb93F28Cfca2b2606d809", 18)],
    [("CELO", "0x471EcE3750Da237f93B8E339c536989b8978a438", 18),
    ("pCELO", "0xE74AbF23E1Fdf7ACbec2F3a30a772eF77f1601E1", 18)],
    [("cEUR", "0xD8763CBa276a3738E6DE85b4b3bF5FDed6D6cA73", 18),
    ("pEUR", "0x56072D4832642dB29225dA12d6Fd1290E4744682", 18)],

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
    with open("PoofDeploys.csv", 'a') as fp:
        fp.write(f'{"/".join(tokenNames)},{",".join(tokens)},{swap.address},{swap.getLpToken()}' + "\n")


def main():
    network.gas_limit(8000000)
    admin = accounts.load('dev-1')

    for pair in COINS:
        names = [x[0] for x in pair]
        tokens = [x[1] for x in pair]
        decimals = [x[2] for x in pair]
        deployPool(tokens, decimals, names, admin)