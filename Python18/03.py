def encrypt_caesar(msg, shift=3):
    little= msg.lower()
    shifted = ''.join([chr(ord(c) + shift) for c in little])
    return ''.join([chr(ord(c)) for c in shifted])


def decrypt_caesar(msg, shift=3):
    little = msg.lower()
    shifted = ''.join([chr(ord(c) - shift) for c in little])
    return ''.join([chr(ord(c)) for c in shifted])


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted,
shift)
print(encrypted)


print(decrypted)
print(" ")
msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted,
shift)
print(encrypted)
print(decrypted)