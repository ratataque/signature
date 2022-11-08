import rsa
import hashlib

pubkey, privkey = rsa.newkeys(1024)
with open('priv.pem', 'rb') as f:
    #print(f.read())
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
with open('pub.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("pub.pem", "wb") as f:
    f.write(pubkey.save_pkcs1("PEM"))
with open("priv.pem", "wb") as f:
    f.write(privkey.save_pkcs1("PEM"))


message = "zebi"

hash = hashlib.sha256(message.encode())

signature = rsa.sign(message.encode(), privkey, "SHA-256")

message = "zebi"

print(rsa.verify(message.encode(), signature, pubkey) == "SHA-256")

