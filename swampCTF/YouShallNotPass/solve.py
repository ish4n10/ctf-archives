import string

data = [
    0xDD, 0x9A, 0xDE, 0x4E, 0x69, 0xE1, 0xE9, 0x2C,
    0xD2, 0x4E, 0xEC, 0xE7, 0x18, 0x26, 0x6A, 0x56,
    0x79, 0xD8, 0xA3, 0x55, 0x72, 0xBC, 0x76, 0xC4,
    0x0C, 0x0F, 0x9B, 0xBE, 0xC6, 0x81, 0xE2, 0x41,
    0x47, 0xA0, 0xF4, 0x26
]


def reverse_xor(data):
    decrypted = []
    rax = 1
    for i in range(len(data)):
        rax = (rax * 0x14A + 0x64) 
        rdi = ((rax * 0xC74F08C9) >> 32) 
        r8d = (rax - rdi) >> 1
        r8d += rdi
        r8d >>= 11
        rdi = r8d * 0x8FF
        rax = rax - rdi
        xor_key = rax & 0xFF  # The last byte of rax
        original_byte = data[i] ^ xor_key
        decrypted.append(original_byte)
    return decrypted

password_bytes = reverse_xor(data)
password_str = ''.join(chr(b) for b in password_bytes)
print("Decrypted Password:", password_str)