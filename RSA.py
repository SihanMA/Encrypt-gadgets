from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 加载公钥和私钥
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=b'mypassword',
        backend=default_backend()
    )

# 加密消息
message = "Hello, World!".encode("utf-8")
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print('加密后的消息:', ciphertext)

# ciphertext = b"S82\xafvO\xe8\x00\xe9\x0e\x9b\xa3\x16}\x19\xcd\x06\xd6#\xbe\xab\xdf\xd2\x9d\x8avv\xa1\x7fj\xdc\xef\xdf\xe4\x01\xc9@\xd2\xdcx\x19\x81<\xc4p\xdc\xc6{?\xce\xcf\xdfi\xd9\xe3\xb9\x84\xa7\xfa\xb4\xebLNv\xb8\x94\x88\x8d\x05\xc2G\x04\x96\x1f\x0c\x87\xado\x02\x1f\xc7TT\x0e\xd1)Xp\\\x90\x99\x06\xe0\xd75\xc9\xd8\xf3\x13\x9b=Q$\xd0\xddn\x8aC\xad\xce*\x02\xe2y\xae]vvl\x11\x08\xeeZ\xd8\xae\xd7\x99\xb4\x1e\xf7\xcc&\x1b:\xd9\xc8\xf53D\x97wI\xbd\xde\xa4\xfeI\xfd`AE\x86\xf7\xd1_\xe1\xe1\x1d\x80O\xc3~\xf7\xf4\x9cbX\xed\x97\xf3y\xa1\x9d\x81\r\\N\x94\xd1n7\xe5\xb6\xd9\xe7\xc8\xe7\x7f\xceW\xe4<\x0c\xa3C\xc8h\xeaG\x10\xb2Q\xe8T\x10\x1f\x93l\t\xb6\xa3\xff\x0c\xe3v\x81i?\xb1V)k\x88P\xcf9w\xfbZ\xc1\xd44\x138s\x8c+'\xc6S\x98\xff\ns\x00\xdbkv\xd0Go5\xab\xcf9f"

# 解密消息
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print('解密后的消息:', plaintext.decode("utf-8"))
