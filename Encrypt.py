import json
import os
import glob
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib
import re

def evp_kdf(password, salt, key_size=32, iv_size=16, iterations=1):
    """OpenSSL EvpKDF - 与CryptoJS兼容的密钥派生函数"""
    target_key_size = key_size + iv_size
    derived_bytes = b""
    block = None
    while len(derived_bytes) < target_key_size:
        hasher = hashlib.md5()
        if block:
            hasher.update(block)
        hasher.update(password)
        hasher.update(salt)
        block = hasher.digest()
        for _ in range(1, iterations):
            hasher = hashlib.md5()
            hasher.update(block)
            block = hasher.digest()
        derived_bytes += block
    return derived_bytes[:target_key_size]

def encrypt_ogame_save(data):
    """加密OGame存档数据"""
    try:
        password = b"ogame-vue-ts"
        salt = get_random_bytes(8)
        
        # 使用EvpKDF派生密钥和IV
        derived_key = evp_kdf(password, salt, 32, 16, 1)
        key = derived_key[:32]
        iv = derived_key[32:]
        
        # 加密数据
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # 将数据转为JSON字符串
        if isinstance(data, str):
            plaintext = data.encode('utf-8')
        else:
            plaintext = json.dumps(data, ensure_ascii=False).encode('utf-8')
        
        # PKCS7填充
        padding_length = 16 - (len(plaintext) % 16)
        padded_data = plaintext + bytes([padding_length] * padding_length)
        
        encrypted = cipher.encrypt(padded_data)
        
        # 组合salt和加密数据，添加CryptoJS前缀
        combined = b'Salted__' + salt + encrypted
        return base64.b64encode(combined).decode('utf-8')
        
    except Exception as e:
        print(f"加密失败: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None