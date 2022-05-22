from Pyfhel import Pyfhel

class Ckks:
    def __init__(self):
        self.HE = Pyfhel()  # Pyfhel object is created

        ckks_params = {
            'scheme': 'CKKS',  # Scheme : BFV / CKKS
            'n': 2 ** 14,  # num. of slots per plaintext
            'scale': 2 ** 30,  # to round the floating point number
            'qi': [60, 30, 30, 30, 60]  # Number of bits of each prime
        }

        self.HE.contextGen(**ckks_params)
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
    obj = Ckks()

    cx, cy = obj.encrypt(x=[1.1, 2.2], y=[3.3, 4.4])

    obj.decrypt("cx", cx)
    obj.decrypt("cy", cy)
    
    csum = cx + cy
    cmul = cx * cy
    csub = cx - cy

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
