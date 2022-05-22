from Pyfhel import Pyfhel

class Bfv:
    def __init__(self):
        self.HE = Pyfhel()  # Pyfhel object is created
        bfv_params = {
            'scheme': 'BFV',  # Scheme : BFV / CKKS
            'n': 2 ** 13,  # num. of slots per plaintext
            't': 65537,  # Plaintext modulus
            't_bits': 20,  # Number of bits in t
            'sec': 128,  # Security parameter, Higher the number slow computation
        }

        self.HE.contextGen(**bfv_params)
        self.HE.keyGen()  # Generate public/secret keys
        self.HE.relinKeyGen()  # generate a relin key


    def encrypt(self, **data):

        # Encryption
        x = self.HE.encrypt(data["x"])
        y = self.HE.encrypt(data["y"])

        print(f"Cipher text of {data['x']} > {x}")
        print(f"Cipher text of {data['y']} > {y}\n")

        return x, y

    def decrypt(self, msg, ctext):

        # Decryption
        r = self.HE.decrypt(ctext)

        print(f"Decryption of {msg} > {r}\n")


if __name__ == "__main__":
    obj = Bfv()

    cx, cy = obj.encrypt(x=[3], y=[5])

    csum = cx + cy
    cmul = cx * cy
    csub = cx - cy

    obj.decrypt("cx", cx)
    obj.decrypt("cy", cy)
    obj.decrypt("csum (cx + cy)", csum)
    obj.decrypt("csub (cx - cy)", csub)

    print(f"before relinearization (cmul) {cmul}")

    ~cmul

    print(f"after relinearization (cmul) {cmul}\n")

    obj.decrypt("cmul (cx * cy)", cmul)
    
    _3xy = ~(3 * cx * cy)
    obj.decrypt("3xy", cy)

    eq = _3xy + cx
    obj.decrypt("Equation Result", eq)
