from ecdsa import SigningKey, VerifyingKey, NIST256p

class ECDSASignature:
    def __init__(self):  # Fixed method name
        self.signing_key = SigningKey.generate(curve=NIST256p)
        self.verifying_key = self.signing_key.get_verifying_key()

    def sign(self, data: bytes) -> bytes:
        return self.signing_key.sign(data)

    def verify(self, data: bytes, signature: bytes) -> bool:
        try:
            return self.verifying_key.verify(signature, data)
        except:
            return False

# Test the functionality
if __name__ == "__main__":
    ecdsa = ECDSASignature()
    test_data = b"Hello, ECDSA!"

    # Sign the data
    print("Signing the data...")
    signature = ecdsa.sign(test_data)
    print(f"Signature: {signature.hex()}")

    # Verify the signature
    print("\nVerifying the signature...")
    is_valid = ecdsa.verify(test_data, signature)
    print(f"Signature valid: {is_valid}")
