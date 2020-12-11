# Can COViD steal Bob's idea?

> Bob wants Alice to help him design the stream cipher's keystream generator base on his rough idea. Can COViD steal Bob's "protected" idea? 

We were provided a `.pcapng` file and a description suggesting that the challenge involves a stream cipher — this information will be important for a later challenge.

## PCAP Static Analysis

Opening `crypto-challenge-1.pcapng` with Wireshark and applying the display filter `data.len > 1` will show the captured data packets. As the number of such packets is small, it is feasible to look through them manually and extract any interesting data.

> p = 298161833288328455288826827978944092433 (Packet 22)  
g = 216590906870332474191827756801961881648 (Packet 30)  
g^a = 181553548982634226931709548695881171814 (Packet 36)  
g^b = 64889049934231151703132324484506000958 (Packet 46)

> Hi Alice, could you please help me to design a keystream generator according to the file I share in the file server so that I can use it to encrypt my 500-bytes secret message? Please make sure it run with maximum period without repeating the keystream. The password to protect the file is our shared Diffie-Hellman key in digits. Thanks. (Packet 52)  

In addition to the above messages, there is also a zip file `CryptoDesign.png` which is contained in packets 107 and 109.

## Diffie-Hellman Encryption
From the data obtained via static analysis of `crypto-challenge-1.pcapng`, it is clear that the goal of the challenge is to obtain the password to the encrypted zip file. Furthermore, we are told that the password is a **Diffie-Hellman** key. The parameters provided (`p, g, g^a & g^b)` also correspond to those used in 
the Diffie–Hellman protocol, providing further confirmation.  
Diffie-Hellman (Diffie-Hellman key exchange) is an implementation of public key cryptography that predates RSA. The shared secret (the key) can be computed as follows:
``s = B^a mod p`` OR ``s = A^b ``, where ``A = g^a % p`` and ``B = g^b % p``
As the private keys (`a` & `b`) are not provided, we have to solve either ``A = g^a % p`` or ``B = g^b % p``. Suppose we decide for solve for `a`. From the aforementioned equation, we have ``a = log(A, base = g) % p``. This is equivalent to solving the [discrete logarithm problem](https://en.wikipedia.org/wiki/Discrete_logarithm_problem) for `a`. Unfortunately, there is no efficient means of computing the discrete logarithm in general. However, we can make the following observations regarding the public modulus `p`:
1. It is small (128 bits)
2. `p-1` has small prime factors (`` p-1 =  2^4 × 3^4 × 19 × 89 × 263 × 23 292263  × 8131 686029  × 2 731211 959087 ``)

These properties allows us to employ the **Pohlig-Hellman** algorithm to compute the discrete logarithm. Using an [online calculator that implements the Pohlig-Hellman algorithm](https://www.alpertron.com.ar/DILOG.HTM), we obtain ``a = 211631375588570729261040810141700746731``.  
Since we have now computed `a`, we can plug it into the equation ``s = B^a mod p``, to obtain our shared key ``s``.
```python
>>> a=211631375588570729261040810141700746731
>>> B=64889049934231151703132324484506000958
>>> p=298161833288328455288826827978944092433
>>> pow(B,a,p)
246544130863363089867058587807471986686
```
The flag is therefore ``govtech-csg{246544130863363089867058587807471986686}``

## Conclusion
The challenge involved static analysis of a ``.pcapng`` file, as well as usage of the Pohlig-Hellman algorithm to compute a discrete logarithm. We found the challenge refreshing as the majority of cryptography challenges involving public-key encryption that we have previously encountered utilise RSA. From this, we learned more about the Diffie-Helman cryptosystem, as well as the importance of having sufficiently large prime exponents.
