import hashlib

class Block:
    def __init__(self, transactions, timeStamp, previousHash=''):
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        return hashlib.sha256((str(self.nonce) + self.previousHash + str(self.transactions) + str(self.timeStamp)).encode('utf-8')).hexdigest()

    def mineBlock(self, difficulty):
        while(self.hash[0:difficulty] != '0'*difficulty):
            self.nonce += 1
            self.hash = self.calculateHash()

        print("Block mined: ", self.hash)

    def toString(self):
        return self.previousHash + str([b.toString() for b in self.transactions]) + str(self.timeStamp)