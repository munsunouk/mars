import json
from pathlib import Path
import os

class Pool(object) :

    def __init__(self) :

        self.id = None
        self.name = None
        self.contract = None
        self.decimal = None
        self.tokenA = None
        self.tokenB = None
        
    def set_pool(self, chainName : str = '', exchangeName : str = '') -> dict :

        basePath = 'src'
    
        marketDictPath = os.path.join(basePath, "list", "market_list.json")
        
        if Path(marketDictPath).exists() :
            with open(marketDictPath, "rt", encoding="utf-8") as f:
                marketDict = json.load(f)
        else :
            print("marketDictPath doesnt exist")
            return {}
    
        poolDictPath = os.path.join(basePath, "list", "pool_list.json")
        
        if Path(poolDictPath).exists() :
            with open(poolDictPath, "rt", encoding="utf-8") as f:
                poolDict = json.load(f)
        else :
            print("poolDictPath doesnt exist")
            return {}
        
        market = marketDict[exchangeName]
            
        poolAvailable = market["pools"]
        
        exchangePool = {}
        
        for pool in poolAvailable :
            
            if isinstance(poolDict[pool], dict) :
                
                exchangePool[pool] = poolDict[pool]
                exchangePool[pool]["contract"] = exchangePool[pool]["contract"][exchangeName]
            
        return exchangePool
