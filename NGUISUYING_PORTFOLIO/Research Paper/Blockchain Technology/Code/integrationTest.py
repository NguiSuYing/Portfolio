import unittest
import json
from blockchain import Blockchain

class TestBlockchainIntegration(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_full_blockchain_workflow(self):
        # Add a transaction and create a block
        self.blockchain.new_transaction("sender_address", "recipient_address", 5)
        self.blockchain.new_transaction("sender_address_2", "recipient_address_2", 10)
        self.blockchain.new_transaction("sender_address_3", "recipient_address_3", 15)
        
        # Check that 4 blocks exist (including genesis block)
        self.assertEqual(len(self.blockchain.chain), 4)
        
        # Check the transactions in the latest block
        last_block = self.blockchain.last_block
        self.assertEqual(len(last_block['transactions']), 1)
        self.assertEqual(last_block['transactions'][0]['sender'], "sender_address_3")
        self.assertEqual(last_block['transactions'][0]['recipient'], "recipient_address_3")
        self.assertEqual(last_block['transactions'][0]['amount'], 15)
        
        # Verify blockchain integrity
        for i in range(1, len(self.blockchain.chain)):
            current_block = self.blockchain.chain[i]
            previous_block = self.blockchain.chain[i - 1]
            self.assertEqual(current_block['previous_hash'], self.blockchain.hash(previous_block))
    
    def test_multiple_transactions(self):
        # Add multiple transactions
        self.blockchain.new_transaction("sender_address_1", "recipient_address_1", 10)
        self.blockchain.new_transaction("sender_address_2", "recipient_address_2", 20)
        
        # Check that 3 blocks exist (including genesis block)
        self.assertEqual(len(self.blockchain.chain), 3)
        
        # Check the transactions in the latest block
        last_block = self.blockchain.last_block
        self.assertEqual(len(last_block['transactions']), 1)
        self.assertEqual(last_block['transactions'][0]['sender'], "sender_address_2")
        self.assertEqual(last_block['transactions'][0]['recipient'], "recipient_address_2")
        self.assertEqual(last_block['transactions'][0]['amount'], 20)

    def test_blockchain_integrity(self):
        # Add a transaction and create a block
        self.blockchain.new_transaction("sender_address", "recipient_address", 5)
        
        # Verify blockchain integrity
        for i in range(1, len(self.blockchain.chain)):
            current_block = self.blockchain.chain[i]
            previous_block = self.blockchain.chain[i - 1]
            self.assertEqual(current_block['previous_hash'], self.blockchain.hash(previous_block))
            self.assertTrue(self.blockchain.valid_proof(previous_block['proof'], current_block['proof']))

if __name__ == '__main__':
    unittest.main()
