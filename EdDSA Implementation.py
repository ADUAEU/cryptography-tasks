from nacl.signing import SigningKey as EdSigningKey
from nacl.encoding import HexEncoder

class EdDSASignature:
    def __init__(self):  # Fixed method name
        self.signing_key = EdSigningKey.generate()
        self.verify_key = self.signing_key.verify_key

    def sign(self, data: bytes) -> bytes:
        # Signs the data and returns the signed message (signature + message)
        return self.signing_key.sign(data)

    def verify(self, signed_message: bytes) -> bool:
        try:
            # Verifies the signed message
            self.verify_key.verify(signed_message)
            return True
        except:
            return False

# Test the functionality
if __name__ == "__main__":
    eddsa = EdDSASignature()
    test_data = b"Hello, EdDSA!"

    # Sign the data
    print("Signing the data...")
    signed_message = eddsa.sign(test_data)
    print(f"Signed Message: {signed_message.hex()}")

    # Verify the signed message
    print("\nVerifying the signed message...")
    is_valid = eddsa.verify(signed_message)
    print(f"Signature valid: {is_valid}")
