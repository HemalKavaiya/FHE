# FHE
Implementation of Encryption and Decryption in Homomorphic Encryption Algorithm.

## Used [Pyfhel](https://github.com/ibarrond/Pyfhel) library in python 

which includes 
1) **BFV** Scheme which is more suited for arithmetic on integers and decrpt the exact result
2) **CKKS** Scheme which is more suited for arithmetic on real numbers and give approximate close result. 
and it also provides bootstrapping for CKKS.

And Uses [Microsoft SEAL](https://github.com/microsoft/SEAL) as a Backend.

---

Object of Pyfhel is Created using
> HE = Pyfhel()

Keys are Generated using
> HE.keyGen()

---


### For Example let **x = 3** and **y = 5** in BFV Scheme :-
Cipher text:

```python
cx, cy = obj.encrypt(x=[3], y=[5])
```

Addition, Multiplication and Subtraction:
```python
csum = cx + cy
cmul = cx * cy
csub = cx - cy
```

<br>
<p> Ciphertext-ciphertext multiplications increase the size of the polynoms 
representing the resulting ciphertext. To prevent this growth, the 
relinearization technique is used (typically right after each c-c mult) to 
reduce the size of a ciphertext back to the minimal size.
For this, a special type of public key called Relinearization Key is used.

Initializing Relinearization Key
> HE.relinKeyGen() 
  
And to relinearize a multiplication **~** sign is used
</p>
</br>



> Before using **~cmul** :- <Pyfhel Ciphertext at 0x1d8043f0840, scheme=bfv, size=3/3, noiseBudget=114>

```python
~cmul
```

> After using **~cmul** :- <Pyfhel Ciphertext at 0x1d8043f0840, scheme=bfv, size=2/3, noiseBudget=114>

<br>

Decryption :-
> BFV Scheme gives exact result
```python
obj.decrypt("csum (cx + cy)", csum)
Decryption of csum (cx + cy) > [8 0 0 ... 0 0 0]

obj.decrypt("csub (cx - cy)", csub)
Decryption of csub (cx - cy) > [-2  0  0 ...  0  0  0]

obj.decrypt("cmul (cx * cy)", cmul)
Decryption of cmul (cx * cy) > [15  0  0 ...  0  0  0]
```

---

### Example with CKKS Scheme :-
`Equation`
> Encrypt(3xy + x) = Encrypt(3xy) + Encrypt(x) = [3 * Encrypt(x) * Encrypt(y)] + Encrypt(x)

Encryption
```python
cx, cy = obj.encrypt(x=[1.1, 2.2], y=[3.3, 4.4])
```

3xy = [3 * Encrypt(x) * Encrypt(y)]
```python
_3xy = ~(3 * cx * cy)
```

Encrypt(3xy + x) = Encrypt(3xy) + Encrypt(x)
```python
eq = _3xy + cx
```

Decryption :-
```python
obj.decrypt("Equation Result", eq)
Decryption of Equation Result > [ 1.19936477e+01  3.12497888e+01  1.12081209e-06 ...  1.08117709e-05 -1.27877279e-06 -3.55203472e-06]
```
