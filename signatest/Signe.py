
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding



try:
    with open("private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
except:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    privkey = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private.pem', 'wb') as f:
        f.write(privkey)



with open("message.txt", "rb") as f:
    message = f.read()

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print(signature+message)

message = signature + b"zebi" + message


with open('messageSigne.txt', 'wb') as f:
    f.write(message)

print("message signé avec succès !", "lancez Verif.py pour vérifier la signature")
