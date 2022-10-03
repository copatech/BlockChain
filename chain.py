import hashlib
from block import Block

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []
        self.First_Block()

    def Proof_of_Work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256-self.difficulty) and block.previous_hash == self.blocks[-1].hash
            

    def Add_to_Chain(self, block):
            if self.Proof_of_Work(block):
                self.blocks.append(block)


    def Add_to_Pool(self, data):
            self.pool.append(data)

    def First_Block(self):
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        first = Block('First', h)
        first.mine(self.difficulty)
        self.blocks.append(first)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.Add_to_Chain(block)
        
            print('\n\n==============')
            print('Hash:\t\t', block.hash.hexdigest())
            print('Previous Hash:\t\t', block.previous_hash.hexdigest())
            print('Nonce:\t\t', block.nonce)