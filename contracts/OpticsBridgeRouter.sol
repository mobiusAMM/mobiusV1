// SPDX-License-Identifier: MIT OR Apache-2.0
// This contract was made by the Optics team and is here merely for compilation reasons
pragma solidity >=0.6.11;

/**
 * @title BridgeRouter
 */
interface BridgeRouter {
    // ============ Libraries ============

    /**
     * @notice Send tokens to a recipient on a remote chain
     * @param _token The token address
     * @param _amount The token amount
     * @param _destination The destination domain
     * @param _recipient The recipient address
     */
    function send(
        address _token,
        uint256 _amount,
        uint32 _destination,
        bytes32 _recipient
    ) external;
}