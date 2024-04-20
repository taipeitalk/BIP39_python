import os
import hashlib
import binascii
from mnemonic import Mnemonic

# 生成256位随机熵
entropy = os.urandom(32)
entropy_hex = binascii.hexlify(entropy).decode('utf-8')
print("随机熵（256位）:", entropy_hex)

# 计算SHA-256哈希，取前面的几位作为校验和
hash_sha256 = hashlib.sha256(entropy).digest()
hash_hex = binascii.hexlify(hash_sha256).decode('utf-8')
checksum_bit_length = len(entropy) * 8 // 32
checksum = bin(int(hash_hex, 16))[2:].zfill(256)[:checksum_bit_length]
print("校验和:", checksum)

# 将随机熵与校验和组合
# 将校验和转换为十六进制字符串
checksum_hex = '{:0>2x}'.format(int(checksum, 2))

# 将随机熵与校验和组合（不需要解码）
combined = entropy_hex + checksum_hex
print("组合后的熵和校验和:", combined)

# 生成助记词
mnemo = Mnemonic("english")
mnemonic_words = mnemo.to_mnemonic(entropy)
print("助记词:", mnemonic_words)
