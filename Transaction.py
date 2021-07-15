import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

class Transaction:
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.signature = ''
    
    def generateHash(self):
        return hashlib.sha256((str(self.fromAddress)+self.toAddress+str(self.amount)).encode('utf-8')).hexdigest()

    def signTransaction(self, signingKey):
        if(signingKey.getPublicKey() != self.fromAddress):
            raise Exception("signing transaction for other wallet is not allowed")

        hashTransaction = self.generateHash()
        sign = signingKey.sign(hashTransaction) #, ec.ECDSA(hashes.SHA256()).hex())
        self.signature = sign

    def checkValidity(self):
        if(self.fromAddress == None or len(self.fromAddress) == 0):
            return True
        if(self.signature or len(self.signature)==0):
            raise Exception("No signature found.")

        

    def toString(self):
        return str(self.fromAddress)+" => "+self.toAddress+" : "+str(self.amount)