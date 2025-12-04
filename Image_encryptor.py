from PIL import Image
import numpy as np


class ImageEncryptor:
    def __init__(self, filename="ab.jpg"):
        # Load image "ab" automatically
        self.image = Image.open(filename).convert("RGB")
        self.data = np.array(self.image).astype("uint8")

    # -----------------------------------------------------
    # 1. Pixel Swap Encryption
    # -----------------------------------------------------
    def encrypt_swap(self):
        encrypted = self.data.copy()
        h, w, _ = encrypted.shape

        # Swap pixel (x) with (x+1) for every pair
        for y in range(h):
            for x in range(0, w - 1, 2):
                encrypted[y, x], encrypted[y, x + 1] = encrypted[y, x + 1], encrypted[y, x]

        return Image.fromarray(encrypted)

    def decrypt_swap(self):
        # Swap operation is reversible by applying again
        return self.encrypt_swap()

    # -----------------------------------------------------
    # 2. Math-based Encryption (simple add key)
    # -----------------------------------------------------
    def encrypt_math(self, key=50):
        encrypted = (self.data + key) % 256
        return Image.fromarray(encrypted.astype("uint8"))

    def decrypt_math(self, key=50):
        decrypted = (self.data - key) % 256
        return Image.fromarray(decrypted.astype("uint8"))

    # -----------------------------------------------------
    # Save helper
    # -----------------------------------------------------
    @staticmethod
    def save(img, path):
        img.save(path)
        print(f"Saved: {path}")
