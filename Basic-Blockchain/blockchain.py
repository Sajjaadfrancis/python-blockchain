import hashlib
import json
from time import time

#chain - has empty list which we add blocks to
#pending transactions - sit in this array until approved and moved to a new block
class Blockchain():
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.newBlock(previousHash="Not sure about anything these days", proof=100)
        
#index - add 1 to the length of the blockchain, eg, genesis block has index = 1
#timestamp - shows time the block was created
#proof - 
#previous hash - hashed version of the previous approved block
    def newBlock(self, proof, previousHash=None):
        block = {
            'index': len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.pendingTransactions,
            'proof': proof,
            'previousHash': previousHash or self.hash(self.chain[-1])
        }
#add above properties to the chain
        self.pendingTransactions = []
        self.chain.append(block)
        return block

#lastblock method - to call the chain and receive the most recently added block
    @property
    def lastBlock(self):
        return self.chain[-1]

#show sender, recipient and amount, basic vars for a transaction
    def newTransaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
 #add details to pending transactions until a new block is added to the blockchain
        self.pendingTransactions.append(transaction)
        return self.lastBlock['index'] +1

#create a hash, which protects data and references the previous block in the blockchain
    def hash(self, block):
#converts key pairs into strings
        stringObject = json.dumps(block, sort_keys=True)
#turn string into unicode
        blockString = stringObject.encode()
#create hexidecimal string
        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()
        return hexHash

#initialize an instance and run dummy transactions
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



