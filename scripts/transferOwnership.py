import requests
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import (
    accounts,
    network,
)

SWAP_ADDRESS = "0xa95B3abe4834b7310a0F12f67c35F73dbDc53a87"

pools = [
    '0x0ff04189Ef135b6541E56f7C638489De92E9c778'
    '0xdBF27fD2a702Cc02ac7aCF0aea376db780D53247',
    '0xE0F2cc70E52f05eDb383313393d88Df2937DA55a',
    '0x19260b9b573569dDB105780176547875fE9fedA3',
    '0xA5037661989789d0310aC2B796fa78F1B01F195D',
    '0x2080AAa167e2225e1FC9923250bA60E19a180Fb2',
]

mobius_sig = '0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c'

def main():
    network.gas_limit(8000000)
    admin = accounts.load('kyle_personal')
    
    for pool in pools:
        pool.setDevAddress(mobius_sig, {"from": admin})
        pool.transferOwnership(mobius_sig, {"from": admin})
