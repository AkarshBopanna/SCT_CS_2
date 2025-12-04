from image_encryptor import ImageEncryptor

# Automatically loads "ab.jpg" from the same folder
enc = ImageEncryptor("ab.jpg")

# ---------------------
# Swap Encryption
# ---------------------
encrypted_swap = enc.encrypt_swap()
enc.save(encrypted_swap, "encrypted_ab.png")

decrypted_swap = ImageEncryptor("encrypted_ab.png").decrypt_swap()
enc.save(decrypted_swap, "decrypted_ab.png")

# ---------------------
# Math Encryption
# ---------------------
encrypted_math = enc.encrypt_math(key=123)
enc.save(encrypted_math, "encrypted_ab_math.png")

decrypted_math = ImageEncryptor("encrypted_ab_math.png").decrypt_math(key=123)
enc.save(decrypted_math, "decrypted_ab_math.png")
