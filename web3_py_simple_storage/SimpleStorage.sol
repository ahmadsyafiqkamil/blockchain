// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;
contract simpleStorage {
    
    // uint256 favNumber = 5;
    // bool favBool = false;
    // string favString = "hello solidity";
    // int256 favInt = -19;
    // address favAddress = 0x7ea3C3B6C545C758446D3f93D308a6940Fcf1ebC
    // bytes32 favBytes = "cat"
    
    
    uint256 favNumber ;
    
    struct People {
        uint256 favNumber;
        string name;
    }
    
    // People public syafiq = People({favNumber:10,name:"syafiq"}); 
    People [] public people; 
    mapping (string => uint256) public nameToFavNumber; 
    
    function store(uint256 _favNumber) public returns(uint256){
        favNumber = _favNumber;
        // uint256 test = 4;
        return favNumber;
    }
    
    function retrive() public view returns (uint256) {
        return favNumber;
    }
    
    function addPerson(string memory _name,uint256 _favNumber) public {
        people.push(People( _favNumber, _name));
        nameToFavNumber[_name] = _favNumber;
    }
    
}