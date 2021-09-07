// SPDX-License-Identifier: MIT

pragma solidity 0.6.12;

import './openzeppelin-contracts@3.4.0/contracts/token/ERC20/IERC20.sol';
import './openzeppelin-contracts@3.4.0/contracts/token/ERC20/ERC20.sol';
import './openzeppelin-contracts@3.4.0/contracts/math/SafeMath.sol';

// This contract handles swapping to and from xNRV, Nerve's staking token.
contract xNerve is ERC20("xNerve", "xNRV"){
    using SafeMath for uint256;
    IERC20 public nerve;

    // Define the Nerve token 
    constructor(IERC20 _nerve) public {
        nerve = _nerve;
    }

    // Enter the bar. Pay some Nerves. Earn some shares.
    // Locks Nerve and mints xNerve
    function enter(uint256 _amount) public {
        // Gets the amount of Nerve locked in the contract
        uint256 totalNerve = nerve.balanceOf(address(this));
        // Gets the amount of xNerve in existence
        uint256 totalShares = totalSupply();
        // If no xNerve exists, mint it 1:1 to the amount put in
        if (totalShares == 0 || totalNerve == 0) {
            _mint(msg.sender, _amount);
        } 
        // Calculate and mint the amount of xNerve the Nerve is worth. The ratio will change overtime, as xNerve is burned/minted and Nerve deposited + gained from fees / withdrawn.
        else {
            uint256 what = _amount.mul(totalShares).div(totalNerve);
            _mint(msg.sender, what);
        }
        // Lock the Nerve in the contract
        nerve.transferFrom(msg.sender, address(this), _amount);
    }

    // Leave the bar. Claim back your NERVEs.
    // Unlocks the staked + gained Nerve and burns xNerve
    function leave(uint256 _share) public {
        // Gets the amount of xNerve in existence
        uint256 totalShares = totalSupply();
        // Calculates the amount of Nerve the xNerve is worth
        uint256 what = _share.mul(nerve.balanceOf(address(this))).div(totalShares);
        _burn(msg.sender, _share);
        nerve.transfer(msg.sender, what);
    }
}
