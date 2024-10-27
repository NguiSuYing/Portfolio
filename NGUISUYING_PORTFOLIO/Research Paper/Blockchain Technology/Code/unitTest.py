import unittest
from blockchain import Blockchain
import hashlib
import json
from time import time

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        # Test the genesis block
        self.assertEqual(len(self.blockchain.chain), 1)
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block['proof'], 100)
        self.assertEqual(genesis_block['previous_hash'], '1')
        self.assertEqual(genesis_block['transactions'], [])

    def test_new_block(self):
        # Test adding a new block
        previous_block = self.blockchain.last_block
        proof = self.blockchain.proof_of_work(previous_block['proof'])
        new_block = self.blockchain.new_block(proof)
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(new_block['index'], 2)
        self.assertEqual(new_block['previous_hash'], self.blockchain.hash(previous_block))
        self.assertEqual(new_block['transactions'], [])

    def test_new_transaction(self):
        # Test adding a new transaction
        sender = "sender_address"
        recipient = "recipient_address"
        amount = 10
        self.blockchain.new_transaction(sender, recipient, amount)
        self.assertEqual(len(self.blockchain.chain), 2)
        last_block = self.blockchain.last_block
        self.assertEqual(len(last_block['transactions']), 1)
        transaction = last_block['transactions'][0]
        self.assertEqual(transaction['sender'], sender)
        self.assertEqual(transaction['recipient'], recipient)
        self.assertEqual(transaction['amount'], amount)

    def test_proof_of_work(self):
        # Test proof-of-work
        last_proof = self.blockchain.last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        self.assertTrue(self.blockchain.valid_proof(last_proof, proof))

    def test_block_hashing(self):
        # Test block hashing
        block = self.blockchain.last_block
        block_hash = self.blockchain.hash(block)
        self.assertEqual(len(block_hash), 64)
        self.assertIsInstance(block_hash, str)

if __name__ == '__main__':
    unittest.main()
