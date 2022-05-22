# FHE
Implementation of Encryption and Decryption in Homomorphic Encryption Algorithm.

## I used [Pyfhel](https://github.com/ibarrond/Pyfhel) library in python 

which includes 
1) **BFV** Scheme which is more suited for arithmetic on integers and decrpt the exact result
2) **CKKS** Scheme which is more suited for arithmetic on real numbers and give approximate close result. 
and it also provides bootstrapping for CKKS.

And Uses [Microsoft SEAL](https://github.com/microsoft/SEAL) as a Backend.

---

### To Encrypt and Decrypt data first we have to generate Keys
Keys are Generated using
> HE.keyGen()

---

### For Simple Example i used **x = 3** and **y = 5** in BFV Scheme
To retrive cipher text:

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

To initialize Relinearization Key
> relinKeyGen() function is used in Pyfhel
  
And to relinearize a multiplication **~** sign is used like
</p>
</br>



> Before using **~cmul** :- <Pyfhel Ciphertext at 0x1d8043f0840, scheme=bfv, size=3/3, noiseBudget=114>

```python
~cmul
```

> After using **~cmul** :- <Pyfhel Ciphertext at 0x1d8043f0840, scheme=bfv, size=2/3, noiseBudget=114>

<br>

and Decrption was:
> BFV Scheme gives exact result
```python
Decryption of csum (cx + cy) > [8 0 0 ... 0 0 0]
Decryption of cmul (cx * cy) > [15  0  0 ...  0  0  0]
```

---

### Another Example with CKKS Scheme with Below Equation 
> Encrypt(3xy + x) = Encrypt(3xy) + Encrypt(x) = [3 * Encrypt(x) * Encrypt(y)] + Encrypt(x)

Encryption
```python
cx, cy = obj.encrypt(x=[1, 2], y=[3, 4])
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
Decryption of Equation Result > [ 1.00030353e+01  2.60080746e+01 -1.11561587e-06 ... -1.15990726e-06 1.18289616e-06 -2.16752571e-06]
```
