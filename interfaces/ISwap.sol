// SPDX-License-Identifier: MIT

pragma solidity 0.6.12;


interface ISwap {
    function updateUserWithdrawFee(address, uint256) external;
}