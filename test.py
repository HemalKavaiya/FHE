from Pyfhel import Pyfhel
import numpy as np


class Bfv:
    def __init__(self):
        self.HE = Pyfhel()
        self.bfv_params = {
            'scheme': 'BFV',
            'n': 2 ** 13,
            't': 65537,
            't_bits': 20,
            'sec': 128,
        }

        self.HE.contextGen(**self.bfv_params)
        self.HE.keyGen()

    def encrypt(self, **kwargs):
        x = self.HE.encrypt(kwargs["x"])
        y = self.HE.encrypt(kwargs["y"])

        print("\nInteger Encoding & Encryption, ")
        print("x > \t", x)
        print("y > \t", y)

        return x, y

    def decrypt(self, msg, ctext):

        r = self.HE.decryptInt(ctext)

        print(f"Decryption of {msg} > {r}")


if __name__ == "__main__":
    a = Bfv()
    cx, cy = a.encrypt(x=[3], y=[5])
    csum = cx + cy
    cmul = cx * cy
    csub = cx - cy

    a.decrypt("cx", cx)
    a.decrypt("cy", cy)
    a.decrypt("csum (cx + cy)", csum)

    print(f"cMul before relinearization (size {cmul.size()}): {cmul}")
    a.HE.relinKeyGen()
    ~cmul
    print(f"cMul after relinearization (size {cmul.size()}): {cmul}")

    a.decrypt("cmul (cx * cy)", cmul)
    a.decrypt("csub (cx - cy)", csub)


