// SPDX-License-Identifier: MIT
pragma solidity 0.8.13;

contract SimpleStorage {
    uint storageData;

    function get() constant returns(uint) {
        return storageData;
    }

    function set(uint n) public {
        storageData = n;
    }

    function increment(uint n) public {
        storageData = storageData + n;
    }

    function decrement(uint n) public {
        storageData = storageData - n;
    }

}