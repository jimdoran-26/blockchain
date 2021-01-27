#!/user/bin/python
#-*- coding: utf-8
from hashlib import sha3_256
DIFFICULTY=4

def updateHash(*args):
    hashing_text=""; h= sha3_256()
    for arg in args:
        hashing_text+=str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():
    data=None
    hash=None
    nonce=0
    previous_hash="0"*64

    def __init__(self,data,number=0):
        self.data=data
        self.number=number

    def hash(self):
        return updateHash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str('Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n'%(self.number,self.hash(),self.previous_hash,self.data,self.nonce))


class Blockchain():
    difficulty = DIFFICULTY

    def __init__(self,chain=[]):
        self.chain = chain

    def add(self,block):
        self.chain.append({
            'hash':block.hash(),
            'previous':block.previous_hash,
            'number':block.number,
            'data':block.data,
            'nonce':block.nonce
        })

    def mine(self,block):
        try:
            block.previous_hash=self.chain[-1].get('hash')
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block);break
            else:
                block.nonce+=1

def main():
    #block=Block('hello world',1)
    #print(block)
    blockchain = Blockchain()
    database = ['hello world','what is up', 'hello','goodbye']

    num=0
    for data in database:
        num+=1
        blockchain.mine(Block(data,num))

    for block in blockchain.chain:
        print(block)

if __name__=='__main__':
    main()