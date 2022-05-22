from Pyfhel import Pyfhel

class Ckks:
    def __init__(self):
        self.HE = Pyfhel()

        ckks_params = {
            'scheme': 'CKKS',
            'n': 2 ** 14,
            'scale': 2 ** 30,
            'qi': [60, 30, 30, 30, 60]
        }

        self.HE.contextGen(**ckks_params)
        self.HE.keyGen()
        self.HE.relinKeyGen()  # generate a relin key

    def encrypt(self, **data):
        x = self.HE.encrypt(data["x"])
        y = self.HE.encrypt(data["y"])

        print(f"Cipher text of {data['x']} > {x}")
        print(f"Cipher text of {data['y']} > {y}\n")

        return x, y

    def decrypt(self, msg, ctext):

        r = self.HE.decrypt(ctext)

        print(f"Decryption of {msg} > {r}\n")


if __name__ == "__main__":
    obj = Ckks()

    cx, cy = obj.encrypt(x=[1.1, 2.2], y=[3.3, 4.4])

    obj.decrypt("cx", cx)
    obj.decrypt("cy", cy)

    _3xy = ~(3 * cx * cy)
    obj.decrypt("3xy", cy)

    eq = _3xy + cx
    obj.decrypt("Equation Result", eq)