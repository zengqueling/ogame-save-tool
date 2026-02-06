# OGame Save Tool | OGame存档工具

A Python tool for encrypting and decrypting OGame save files. Specifically designed for **OGame-Vue-Ts**, a web-based version of the classic OGame space strategy game.

一个用于加密和解密OGame存档文件的Python工具。专门为 **OGame-Vue-Ts** 网页版游戏设计，这是经典OGame太空策略游戏的网页版本。

## About OGame-Vue-Ts | 关于OGame-Vue-Ts

**OGame-Vue-Ts** is a modern web-based implementation of the classic OGame space strategy game, built with Vue.js and TypeScript. Players build space empires, colonize planets, research technologies, and engage in intergalactic warfare. The game stores player progress in encrypted save files to prevent tampering.

**OGame-Vue-Ts** 是基于Vue.js和TypeScript构建的现代网页版OGame太空策略游戏。玩家可以建立太空帝国，殖民行星，研究科技，并参与星际战争。游戏将玩家进度存储在加密的存档文件中，以防止篡改。

## Features | 功能

- **Encrypt/Decrypt**: Process OGame save data | 加密/解密：处理OGame存档数据
- **CryptoJS Compatible**: Uses compatible encryption algorithms | CryptoJS兼容：使用兼容的加密算法
- **AES-256-CBC**: Secure encryption algorithm | AES-256-CBC：安全的加密算法
- **Mixed JSON Support**: Handles files with both encrypted and plain JSON fields | 混合JSON支持：处理包含加密和明文JSON字段的文件
- **OGame-Vue-Ts Specific**: Tailored for the web version's save format | OGame-Vue-Ts专用：针对网页版的存档格式优化

## Installation | 安装

```bash
pip install -r requirements.txt
```

## Usage | 使用方法

### Encrypt | 加密
```bash
python Encrypt.py input_save_file.txt
```

### Decrypt | 解密
```bash
python Decrypt.py encrypted_save_file.txt
```

### Programmatic Usage | 编程使用

```python
# Encrypt game save data | 加密游戏存档数据
from Encrypt import encrypt_ogame_save
encrypted_data = encrypt_ogame_save(game_save_dict)

# Decrypt game save data | 解密游戏存档数据
from Decrypt import decrypt_ogame_save, process_ogame_json_data
decrypted_data = decrypt_ogame_save(encrypted_data)

# Process mixed JSON with encrypted fields | 处理包含加密字段的混合JSON
processed_data = process_ogame_json_data(json_data_with_encrypted_fields)
```

## Technical Details | 技术细节

- **Algorithm**: AES-256-CBC | 算法：AES-256-CBC
- **Key Derivation**: OpenSSL EvpKDF (MD5, 1 iteration) | 密钥派生：OpenSSL EvpKDF（MD5，1次迭代）
- **Password**: "ogame-vue-ts" (for OGame-Vue-Ts compatibility) | 密码："ogame-vue-ts"（用于OGame-Vue-Ts兼容性）
- **Key Length**: 32 bytes | 密钥长度：32字节
- **IV Length**: 16 bytes | 初始化向量长度：16字节
- **Padding**: PKCS7 | 填充方式：PKCS7
- **Encoding**: Base64 | 编码：Base64

## Files | 文件说明

- `Encrypt.py` - Encryption functions for OGame-Vue-Ts saves | OGame-Vue-Ts存档加密函数
- `Decrypt.py` - Decryption functions with mixed JSON support | 支持混合JSON的解密函数
- `requirements.txt` - Python dependencies | Python依赖包
- `LICENSE` - MIT License | MIT许可证
- `.gitignore` - Git ignore rules | Git忽略规则

## Game Save Format | 游戏存档格式

OGame-Vue-Ts stores game data in JSON format with some fields encrypted using the AES-256-CBC algorithm. This tool can:

OGame-Vue-Ts使用JSON格式存储游戏数据，其中某些字段使用AES-256-CBC算法加密。此工具可以：

- Encrypt entire save files | 加密整个存档文件
- Decrypt encrypted save files | 解密已加密的存档文件
- Process mixed JSON files with both encrypted and plain text fields | 处理包含加密和明文字段的混合JSON文件

## License | 许可证

MIT License - See [LICENSE](LICENSE) for details | MIT许可证 - 详见[LICENSE](LICENSE)文件

## Compatibility | 兼容性

This tool is specifically designed for **OGame-Vue-Ts** web version and may not work with other OGame implementations or versions.

此工具专门为 **OGame-Vue-Ts** 网页版设计，可能不适用于其他OGame实现或版本。