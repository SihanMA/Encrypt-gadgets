# Encrypt-gadgets
加密小工具，实现明文与密文的加解密。

使用方式：

1. 通过generate_priviteAndPublicKey.py产生私钥和公钥，将公钥发给对方，对方通过公钥加密双方要使用的密钥并传回加密后的密钥
2. 通过私钥解密对密钥解密，得到密钥，将密钥存储在password中
3. 运行ui.py，对明文进行加密，对密文进行解密
