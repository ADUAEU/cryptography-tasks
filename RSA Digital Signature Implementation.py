from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class RSASignature:
    def __init__(self, key_size: int = 2048):  # Fixed method name
        self.key = RSA.generate(key_size)
        self.public_key = self.key.publickey()

    def sign(self, data: bytes) -> bytes:
        h = SHA256.new(data)
        signature = pkcs1_15.new(self.key).sign(h)
        return signature

    def verify(self, data: bytes, signature: bytes) -> bool:
        h = SHA256.new(data)
        try:
            pkcs1_15.new(self.public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

# Test the functionality
if __name__ == "__main__":
    rsa = RSASignature()
    test_data = b"Hello, Digital Signature!"

    # Sign the data
    print("Signing the data...")
    signature = rsa.sign(test_data)
    print(f"Signature: {signature.hex()}")

    # Verify the signature
    print("\nVerifying the signature...")
    is_valid = rsa.verify(test_data, signature)
    print(f"Signature valid: {is_valid}")
