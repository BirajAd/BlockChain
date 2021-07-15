from BlockChain import *
from Transaction import *
from Block import *
from keypairgen import *

a = BlockChain()

a.createTransaction(Transaction('keila', 'lucy', 200))
a.createTransaction(Transaction('lucy', 'keila', 50))
a.createTransaction(Transaction('keila', 'raj', 10))
# print("Block 1 being mined ...")
# a.addBlock(Block(index=1, data=30, timeStamp='7/15/2021'))
# print("Block 2 being mined ...")
# a.addBlock(Block(index=2, data=10, timeStamp='7/15/2021'))
# print("Block 3 being mined ...")
# a.addBlock(Block(index=1, data=5, timeStamp='7/15/2021'))

# for i in a.chain:
#     print(i.index,i.hash,i.previousHash,i.data,i.timeStamp)

# a.chain[1].data = 90
# a.chain[1].hash = a.chain[1].calculateHash()

print(a.checkValidation())

print("mining started...")
a.minePendingTransaction('raj-address')
print("Balance of raj: ", a.getBalanceOfAddress('raj-address'))

print("second mining started...")
a.minePendingTransaction('raj-address')
print("Balance of raj: ", a.getBalanceOfAddress('raj-address'))
print("\n")

for b in a.chain:
    print(b.toString())

# kp = KeyPair(0x63bd3b01c5ce749d87f5f7481232a93540acdb0f7b5c014ecd9cd32b041d6f33)
# print("private: ",kp.getPrivateKey(),"\n\n public: ", kp.getPublicKey(), "\n\n sign: ", kp.sign())

