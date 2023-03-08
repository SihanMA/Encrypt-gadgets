import base64
import tkinter as tk
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptionApp:
    def __init__(self,pswd = "my secret password"):
        # 创建主窗口
        self.window = tk.Tk()
        self.window.title("加密解密工具")
        self.pswd = pswd
        self.window.grid_propagate(True)

        # 创建密钥输入框
        self.key_entry = tk.Entry(self.window, width=50)
        self.key_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.key_entry.insert(0,self.pswd)

        # 创建文本输入框
        self.plaintext_entry = tk.Text(self.window, width=50,height=10)
        self.plaintext_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10,ipady=10)

        # 创建文本输出框
        self.ciphertext_entry = tk.Text(self.window, width=50, state='disable',height=10)
        self.ciphertext_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=10,ipady=10)

        # 创建加密按钮
        self.encrypt_button = tk.Button(self.window, text="加密", width=20, command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, padx=5, pady=5)

        # 创建解密按钮
        self.decrypt_button = tk.Button(self.window, text="解密", width=20, command=self.decrypt)
        self.decrypt_button.grid(row=3, column=1, padx=5, pady=5)

        # 运行主循环
        self.window.mainloop()

    def get_key(self,pswd):
        salt = b'some salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = Fernet(base64.urlsafe_b64encode(kdf.derive(pswd)))
        return key

    def encrypt(self):
        # 获取密钥和明文
        key = self.key_entry.get().encode()
        key = self.get_key(key)
        plaintext = self.plaintext_entry.get("1.0",tk.END).encode("utf-8")

        # 生成加密器并加密
        # f = Fernet(key)
        f = key
        ciphertext = f.encrypt(plaintext)
        print(ciphertext)
        print(len(ciphertext))
        # 将密文写入文本输出框
        self.ciphertext_entry.config(state='normal')
        self.ciphertext_entry.delete("1.0", tk.END)
        self.ciphertext_entry.insert("1.0", ciphertext)
        self.ciphertext_entry.config(state='disable')

    def decrypt(self):
        # 获取密钥和密文
        key = self.key_entry.get().encode()
        key = self.get_key(key)
        ciphertext = self.plaintext_entry.get("1.0",tk.END).strip().encode("utf-8")
        print(ciphertext)
        print(len(ciphertext))
        print(type(ciphertext))
        # ciphertext = base64.b64decode(ciphertext)

        # print(ciphertext)
        # print(len(ciphertext))
        # print(type(ciphertext))

        # 生成解密器并解密
        # f = Fernet(key)
        f = key
        plaintext = f.decrypt(ciphertext)
        print(plaintext)
        # 将明文写入文本输出框
        self.ciphertext_entry.config(state='normal')
        self.ciphertext_entry.delete("1.0", tk.END)
        self.ciphertext_entry.insert("1.0", plaintext.decode("utf-8"))
        self.ciphertext_entry.config(state='disable')





if __name__ == "__main__":
    password = "my secret password"
    with open('password.txt', 'rb') as f:
        password = f.read()
    app = EncryptionApp(password)

