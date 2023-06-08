import random

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.generate_public_key()
        self.d = self.generate_private_key()

    def generate_public_key(self):
        e = random.randint(2, self.phi - 1)
        while self.gcd(e, self.phi) != 1:
            e = random.randint(2, self.phi - 1)
        return e

    def generate_private_key(self):
        d = self.modular_inverse(self.e, self.phi)
        return d

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def modular_inverse(self, a, m):
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError("The modular inverse does not exist.")
        else:
            return x % m

    def get_public_key(self):
        return (self.e, self.n)

    def get_private_key(self):
        return (self.d, self.n)


# Get prime numbers from the user
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))

# Create RSA object and generate keys
rsa = RSA(p, q)

# Print the keys
print("Public Key (e, n):", rsa.get_public_key())
print("Private Key (d, n):", rsa.get_private_key())