import hashlib
import json
from time import time

class Blockchain():
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.newBlock(previousHash="Not sure about anything these days", proof=100)

    def newBlock(self, proof, previousHash=None):
        block = {
            'index': len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.pendingTransactions,
            'proof': proof,
            'previousHash': previousHash or self.hash(self.chain[-1])
        }
        self.pendingTransactions = []
        self.chain.append(block)
        return block

    @property
    def lastBlock(self):
        return self.chain[-1]

    def newTransaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pendingTransactions.append(transaction)
        return self.lastBlock['index'] +1

    def hash(self, block):
        stringObject = json.dumps(block, sort_keys=True)
        blockString = stringObject.encode()
        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()
        return hexHash

blockchain = Blockchain()
t1 = blockchain.newTransaction("Sajjaad", "Chad", 'R1000')
t2 = blockchain.newTransaction("Chad", "Sajjaad", 'R200')
t3 = blockchain.newTransaction("Joshua", "Azzi", 'R150')
blockchain.newBlock(12345)

t4 = blockchain.newTransaction("Mike", "Alice", '1 BTC')
t5 = blockchain.newTransaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.newTransaction("Bob", "Mike", '0.5 BTC')
blockchain.newBlock(6789)

print("Genesis block: ", blockchain.chain)



