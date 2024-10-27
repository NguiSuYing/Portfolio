import hashlib
import json
from time import time
import uuid  # For generating nonce

class Blockchain:
    def __init__(self):
        self.chain = []
        # Create the genesis block with an arbitrary proof and previous hash
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None, transaction=None):
        """
        Create a new block and add it to the blockchain
        :param proof: The proof given by the proof-of-work algorithm
        :param previous_hash: Hash of the previous block
        :param transaction: The transaction to include in the block
        :return: The new block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': [transaction] if transaction else [],
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Add a new transaction to the blockchain by creating a new block
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount of the transaction
        :return: The new block that contains this transaction
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'nonce': uuid.uuid4().hex,  # Generate a unique nonce
        }
        # Perform proof-of-work to find a valid proof
        last_proof = self.last_block['proof']
        proof = self.proof_of_work(last_proof)
        # Create a new block with the transaction
        return self.new_block(proof, transaction=transaction)

    @property
    def last_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block
        :param block: Block
        :return: Hash string
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple proof-of-work algorithm:
        Find a number p' such that hash(pp') contains leading 4 zeroes
        :param last_proof: <int> Previous proof
        :return: <int> New proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validate the proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous proof
        :param proof: <int> Current proof
        :return: <bool> True if correct, False if not
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Create the blockchain
blockchain = Blockchain()

# Add a transaction
block1 = blockchain.new_transaction("sender_address", "recipient_address", 5)
block2 = blockchain.new_transaction("sender_address_2", "recipient_address_2", 10)
block3 = blockchain.new_transaction("sender_address_3", "recipient_address_3", 15)

# Display the blockchain
print(json.dumps(blockchain.chain, indent=4))
