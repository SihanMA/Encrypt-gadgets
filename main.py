import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# 密码学安全建议，参考 https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
password = b'my secret password'
salt = b'some salt'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)

key = Fernet(base64.urlsafe_b64encode(kdf.derive(password)))

# 加密
plaintext = '沐阳老哥'.encode('utf-8')
cipher = key.encrypt(plaintext)
print('密文:', cipher)

# 解密
decrypted_text = key.decrypt(cipher)
print('明文:', decrypted_text.decode('utf-8'))
