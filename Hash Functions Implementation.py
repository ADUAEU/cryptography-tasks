import hashlib

class HashFunctions:
    @staticmethod
    def sha256_hash(data: bytes) -> bytes:
        sha256 = hashlib.sha256()
        sha256.update(data)
        return sha256.digest()

    @staticmethod
    def sha3_256_hash(data: bytes) -> bytes:
        sha3_256 = hashlib.sha3_256()
        sha3_256.update(data)
        return sha3_256.digest()

    @staticmethod
    def blake2b_hash(data: bytes) -> bytes:
        blake = hashlib.blake2b()
        blake.update(data)
        return blake.digest()

# Test the functions
if __name__ == "__main__":
    test_data = b"Hello, World!"

    print("Testing SHA-256:")
    print(HashFunctions.sha256_hash(test_data).hex())

    print("\nTesting SHA3-256:")
    print(HashFunctions.sha3_256_hash(test_data).hex())

    print("\nTesting BLAKE2b:")
    print(HashFunctions.blake2b_hash(test_data).hex())
