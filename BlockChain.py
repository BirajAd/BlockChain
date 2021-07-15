from Block import *
from Transaction import *
from datetime import datetime

class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 2
        self.pendingTransactions = []
        self.miningReward = 1

    #first block in chain
    def createGenesisBlock(self):
        return Block(transactions=[], timeStamp='7/14/2021')

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def minePendingTransaction(self, rewardAddress):
        block = Block(timeStamp=datetime.now(), transactions=self.pendingTransactions)
        block.mineBlock(self.difficulty)

        print("Block successfully mined.")
        self.chain.append(block)

        self.pendingTransactions = [
            Transaction(None, rewardAddress, self.miningReward)
        ]

    def createTransaction(self, transaction):
        self.pendingTransactions.append(transaction)

    def getBalanceOfAddress(self, address):
        balance = 0

        for block in self.chain:
            for tran in block.transactions:
                if(tran.fromAddress == address):
                    balance -= tran.amount
                
                if(tran.toAddress == address):
                    balance += tran.amount

        return balance

    # check if the chain is valid
    def checkValidation(self):
        length = len(self.chain)
        for i in range(1, length):
            if(self.chain[i].hash != self.chain[i].calculateHash()):
                return False
            if(self.chain[i-1].hash != self.chain[i].previousHash):
                return False
        return True
