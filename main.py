import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = '-'.join(transaction_list) + '-' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = 'Charly sends 2 NC to Mike'
t2 = 'Anna sends 3.5 NC to Steve'
t3 = 'Daniel sends 1.6 NC to Anna'
t4 = 'Steve sends 0.6 NC to Bob'
t5 = 'Bob sends 3 NC to Charly'
t6 = 'Daniel sends 1 NC to Charly'

initial_block = NeuralCoinBlock('Initial Block', [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)