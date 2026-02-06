# OGame Save Tool | OGame存档工具

A tool for encrypting and decrypting OGame save data with CryptoJS compatibility. | 用于加密和解密OGame存档数据的工具，兼容CryptoJS。

## Features | 功能
- **Encrypt/Decrypt**: Process OGame save data | 加密/解密：处理OGame存档数据
- **CryptoJS Compatible**: Uses compatible encryption algorithms | CryptoJS兼容：使用兼容的加密算法
- **AES-256-CBC**: Secure encryption algorithm | AES-256-CBC：安全的加密算法

## Installation | 安装
```bash
pip install -r requirements.txt
```

## Usage | 使用方法

### Encrypt | 加密
```bash
python Encrypt.py input_file.txt
```

### Decrypt | 解密
```bash
python Decrypt.py encrypted_file.txt
```

## Requirements | 依赖
- Python 3.x
- pycryptodome>=3.15.0

## License | 许可证
MIT License | MIT许可证