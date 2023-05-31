class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode("utf-8"))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("genesis block", "0")

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        new_block = Block(data, prev_hash)
        self.chain.mainend(new_block)


blockchain = Blockchain()

user = Bank("homan", 16, "Male")
