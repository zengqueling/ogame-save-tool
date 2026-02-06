import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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

def decrypt_ogame_save(encrypted_base64):
    """解密OGame存档数据"""
    try:
        encrypted_data = base64.b64decode(encrypted_base64)
        
        if not encrypted_data.startswith(b'Salted__'):
            raise ValueError("不是有效的加密格式")
        
        salt = encrypted_data[8:16]
        encrypted = encrypted_data[16:]
        
        password = b"ogame-vue-ts"
        derived_key = evp_kdf(password, salt, 32, 16, 1)
        key = derived_key[:32]
        iv = derived_key[32:]
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted)
        
        try:
            unpadded = unpad(decrypted, 16)
        except ValueError:
            unpadded = decrypted
        
        result = unpadded.decode('utf-8')
        
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return result
            
    except Exception as e:
        print(f"解密失败: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def process_ogame_json_data(json_data):
    """处理OGame JSON数据，解密其中的加密字段"""
    decrypted_data = {}
    for key, value in json_data.items():
        if isinstance(value, str) and value.startswith("U2FsdGVkX1"):
            print(f"正在解密字段: {key}")
            decrypted_value = decrypt_ogame_save(value)
            if decrypted_value:
                try:
                    decrypted_data[key] = json.loads(decrypted_value)
                except json.JSONDecodeError:
                    decrypted_data[key] = decrypted_value
            else:
                decrypted_data[key] = f"[解密失败: {value[:50]}...]"
        else:
            decrypted_data[key] = value
    return decrypted_data

def save_json_to_markdown(json_data, field_name, md_file, base_indent=0):
    """将JSON数据保存为Markdown格式"""
    def write_json_recursive(data, indent_level=0):
        indent = "  " * (base_indent + indent_level)
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    md_file.write(f"{indent}- **{key}**:\n")
                    write_json_recursive(value, indent_level + 1)
                else:
                    md_file.write(f"{indent}- **{key}**: {value}\n")
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    write_json_recursive(item, indent_level + 1)
                else:
                    md_file.write(f"{indent}- {item}\n")
        else:
            md_file.write(f"{indent}{data}\n")
    
    md_file.write(f"## {field_name}\n\n")
    write_json_recursive(json_data)
    md_file.write("\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            encrypted_data = f.read().strip()
        result = decrypt_ogame_save(encrypted_data)
        if result:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print("解密失败")
    else:
        print("用法: python Decrypt.py <加密文件>")