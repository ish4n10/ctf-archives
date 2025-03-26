import z3 
import datetime


dt = datetime.datetime(2025, 3, 17, 0, 5, 50, tzinfo=datetime.timezone.utc)
timestamp = int(dt.timestamp())


def globus_forbus(it: int, time: int) -> int:
    return it * it * (time % 0xA + it - 5) + (time % 0xA + it - 3) * it * it * it + ((time % 0xA + it - 7) * it)

def squen_shorp(input_str: str, time: int) -> bytes: 
    input_len = len(input_str)
    buffer = bytearray(input_len)

    for i in range(input_len):
        buffer[i] = (ord(input_str[i]) ^ globus_forbus(i, time)) & 255  

    return bytes(buffer)


def reverse_squen_shorp(encoded_hex: str, time: int) -> str:
    encoded_bytes = bytes.fromhex(encoded_hex)


    decoded_chars = []
    for i in range(len(encoded_bytes)):
      decoded_chars.append(encoded_bytes[i] ^ globus_forbus(i, time) & 0xFF)
   
    return decoded_chars


# lol = squen_shorp(data, timestamp).hex()
data = "52a799d113de948dfb5f59a9c0480347a1d1dc6a84d8851d6b21"

print("hexed", data)

reversed = reverse_squen_shorp(data, timestamp)

print(reversed)

for i in range(len(reversed)):

  print(chr(reversed[i]), end='')


