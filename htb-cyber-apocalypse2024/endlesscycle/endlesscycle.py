import struct

xorred_data = b'\xb6\x9e\xad\xc5\x92\xfa\xdf\xd5\xa1\xa8\xdc\xc7\xce\xa4\x8b\xe1\x8a\xa2\xdc\xe1\x89\xfa\x9d\xd2\x9a\xb7'

xor_key = 0xBEEFCAFE  

trimmed_data = xorred_data[:24]
dwords = struct.unpack('<' + 'I' * (len(trimmed_data) // 4), trimmed_data)
original_dwords = [d ^ xor_key for d in dwords]

last_two_bytes = xorred_data[24:]

leftover = struct.unpack("<H", last_two_bytes)[0]
leftover_xored = struct.pack("<I", (leftover ^ xor_key))

original_data = struct.pack('<' + 'I' * len(original_dwords), *original_dwords)

original_data += leftover_xored

print(original_data[0:26])