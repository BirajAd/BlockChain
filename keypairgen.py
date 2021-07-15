from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
import hashlib

# kpair = ec
# private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
# public_key = private_key.public_key()
# # serializing into PEM
# rsa_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
# # rsa_prem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPrivateKeyInfo)
# pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())

# print(rsa_pem.decode('utf-8'))
# print(pem.decode('utf-8'))
# print("Signature: ",private_key.sign(b'98uiooowerwrijfjhwllslsl', ec.ECDSA(hashes.SHA256())).hex())

class KeyPair:
    def __init__(self, private_value):
        self.signature = ''
        self.curve = ec.SECP256R1()
        self.privateKey = ec.derive_private_key(private_value, self.curve, default_backend())
        self.signature_algorithm = ec.ECDSA(hashes.SHA256())
        self.public_key = self.privateKey.public_key()
        

    def getPrivateKey(self):
        # return private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()).hex()
        return self.privateKey.private_numbers().private_value

    def getPublicKey(self):
        # return public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).hex()
        return self.privateKey.public_key().public_bytes(serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint).hex()

    def sign(self, data=hashlib.sha256(('bir'+'nir'+'0').encode('utf-8')).hexdigest().encode('utf-8')):
        return self.privateKey.sign(data, ec.ECDSA(hashes.SHA256())).hex()
    