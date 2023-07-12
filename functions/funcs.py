from functions.requestMaker import requestMaker
from config import config

# for now I think functions can be added here as needed. The contract addresses are in config.py

def getTotalAmountOfBlobbles():
    params = {}
    method = 'getAmountOfBlobbles'
    res = requestMaker(config.BLOBBLE_MAIN_CONTRACT, method, params)['result']

    # res is hex, convert to int
    return int(res, 16)

def getOwnwerOfBlobble(_tokenId):
    params = {
        "_tokenId": _tokenId
    }
        
    method = 'getOwnerOf'
    return requestMaker(config.BLOBBLE_MAIN_CONTRACT, method, params)['result']

def getAllOwnersOfBlobbles():
    print('fetching all owners of blobbles ...')
    returnObject = {}
    
    for i in range(getTotalAmountOfBlobbles()):
        # print(f'fetching owner of blobble {i}')
        returnObject[i] = getOwnwerOfBlobble(hex(i))

    # return the complete dict, so it can be used however needed
    return returnObject
