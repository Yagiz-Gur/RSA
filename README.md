# Table of contents
- [What  is RSA?](#what-is-rsa)
- [How does RSA work?](#how-does-rsa-work)
- [Generating Key](#generating-key)
- [simple-rsa.py](#simple-rsa.py)
- [key-generator.py](#key-generator.py)
- [rsa-gui.py](#rsa-gui.py)
 



# <a id="what-is-rsa">What is RSA?</a> 

![RSA](https://repository-images.githubusercontent.com/188075289/92938f00-a51d-11ea-95a4-a29ba772a729)

RSA (Rivest-Shamir-Adleman) encryption algorithm is a public-key encryption system. This algorithm was developed by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977 and is one of the widely used encryption algorithms today.


The RSA algorithm is based on public-key cryptography, which means it uses different keys for encryption and decryption. This algorithm is built upon the mathematically complex operation of large number multiplication.

As for its operation, the RSA algorithm consists of three steps:

- **Key Generation:** In the first step, the recipient needs to generate a key pair. This pair includes one private key and one public key. The private key is used for decryption operations, while the public key is used for encryption operations.

- **Encryption:** The person encrypting the data uses the recipient's public key to encrypt the data. In this step, the text or data pieces are encrypted using mathematical operations.

- **Decryption:** The recipient decrypts the encrypted data using their private key. The private key has the ability to decrypt the encrypted data through a specific mathematical operation.

The RSA algorithm is used in various application areas such as secure communication, digital signatures, and authentication. It is a popular encryption algorithm, especially for ensuring data security on the internet.


# <a id="how-does-rsa-work">How does RSA work? </a>
The RSA algorithm is based on the mathematical properties of prime numbers and modular arithmetic. Here is a brief explanation of the mathematical background of the RSA algorithm:

- **Key Generation:**
Select two distinct prime numbers, p and q.
Calculate the modulus, N, by multiplying p and q: N = p * q.
Calculate Euler's totient function, φ(N), which is the number of positive integers less than N and relatively prime to N: φ(N) = (p - 1) * (q - 1).
Choose an integer e (1 < e < φ(N)) that is relatively prime to φ(N). This will be the public key exponent.
Calculate the modular multiplicative inverse of e modulo φ(N) to obtain the private key exponent, d. In other words, d satisfies the equation: (d * e) mod φ(N) = 1.
The public key is the pair (N, e), and the private key is the pair (N, d)

-  **Encryption:**
Represent the message as an integer, m, where 0 ≤ m < N.
The encrypted message, c, is calculated using the public key: c = (m^e) mod N. This is performed using modular exponentiation.

- **Decryption:**
The recipient uses the private key to decrypt the encrypted message.
The decrypted message, m, is calculated using the private key: m = (c^d) mod N. Again, modular exponentiation is used.

![Key Generation](https://samsclass.info/141/proj/pRSA1-1.png)

The security of the RSA algorithm relies on the difficulty of factoring large composite numbers. It is computationally challenging to determine the prime factors of a large number, especially if the factors are large prime numbers. This difficulty forms the basis of RSA's security, as the private key is dependent on the prime factors remaining secret.

By using the proper key generation and securely exchanging public keys, the RSA algorithm provides a secure method for encryption and decryption.

# <a id="generating-key"> Generating Key </a>
select two prime number (p and q). let p = 61 and q = 53, you can follow these steps:

1.  Calculate the modulus, N: N = p * q = 61 * 53 = 3233.
    
2.  Calculate Euler's totient function, φ(N): φ(N) = (p - 1) * (q - 1) = 60 * 52 = 3120.
    
3.  Choose a value for the public key exponent, e: e should be a positive integer greater than 1 and less than φ(N) (3120) that is relatively prime to φ(N). In this case, let's choose e = 17.
    
4.  Calculate the modular multiplicative inverse of e modulo φ(N) to obtain the private key exponent, d: d satisfies the equation (d * e) mod φ(N) = 1. In this case, we need to find a value for d such that (d * 17) mod 3120 = 1. Using the extended Euclidean algorithm or other methods, we find that d = 2753.
    
5.  The public key is the pair (N, e): Public key: (3233, 17).
    
6.  The private key is the pair (N, d): Private key: (3233, 2753).
    

Now you have the public key (3233, 17) and the private key (3233, 2753) for the given prime numbers p = 61 and q = 53. These keys can be used for encryption and decryption operations using the RSA algorithm.

# <a id="simple-rsa.py">simple-rsa.py</a>
This code provides a basic command-line interface for encryption and decryption using the RSA algorithm. It allows the user to input text, choose between encryption or decryption, and provide the necessary keys. The program encrypts the text using the RSA algorithm and outputs the encrypted values, or decrypts the encrypted values back to text using the provided keys and displays the decrypted result.


To use this code, people can run it in a Python environment that supports command-line input. The program presents a menu with options for encryption and decryption.

For encryption:

1.  Choose the encryption option.
2.  Enter the text you want to encrypt.
3.  Provide the public key's exponent (`e`) and modulus (`n`).
4.  The program will perform encryption using the RSA algorithm and display the encrypted values.

For decryption:

1.  Choose the decryption option.
2.  Enter the encrypted text as a series of numbers separated by commas and spaces.
3.  Provide the private key's exponent (`d`) and modulus (`n`).
4.  The program will perform decryption using the RSA algorithm and display the decrypted text.

The code handles errors and provides appropriate error messages if invalid input is entered. Users can follow the prompts, input the required information, and obtain the encrypted or decrypted results based on their selection.

1-) select encryption or decryption
![1](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/simple/1.png?raw=true)

2-) enter the text you want to encrypt, the value of the public key 'e', and the value of 'n'.

![2](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/simple/2.png?raw=true)

3-)The program returns the encrypted text to you as an array.

![3](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/simple/3.png?raw=true)

4-)To decrypt the encrypted text, choose the decryption option and enter the text you want to decrypt along with the values of the private key 'd' and 'n'.

![4](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/simple/4.png?raw=true)

5-)The program returns the decrypted text to you.

![5](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/simple/5.png?raw=true)

# <a id="key-generator.py">key-generator.py</a>

The provided code is an implementation of the RSA (Rivest-Shamir-Adleman) algorithm, which is a widely used cryptographic algorithm for generating public and private keys.

The code allows users to input two prime numbers (`p` and `q`). Using these prime numbers, the code generates a pair of public and private keys. The public key (`e` and `n`) can be shared with others to encrypt messages, while the private key (`d` and `n`) must be kept secret and is used for decrypting the encrypted messages.

People can use this code as a starting point to generate their own RSA key pairs for various purposes, such as secure communication or data encryption. Once the keys are generated, the public key can be distributed to others who want to send encrypted messages to the owner of the private key. The owner can use the private key to decrypt those messages.

1-)   Enter the prime numbers you want to use for key generation (p and q). Note: The larger the prime numbers you enter, the more difficult it will be to decrypt for those whom you do not want to read the message.

![1](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/key%20generator/1.png?raw=true)

2-) The program will output the private and public key values for you.

![2](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/key%20generator/2.png?raw=true)


# <a id="rsa-gui.py">rsa-gui.py <a/>

The rsa-gui.py is a PyQt5 application for performing RSA encryption and decryption. It provides a graphical user interface (GUI).

Note: 1.  Make sure you have PyQt5 installed. If not, you can install it using pip: `pip install pyqt5`.

The main functionalities of the application are as follows:
1.  **The GUI window will appear on your screen. It consists of several elements:**
    
    -   *Input text field:* This is where you can enter the text you want to encrypt.
    -   *Output text field:* This is where the encrypted or decrypted text will be displayed.
    -   *Encrypt button:* Clicking this button will encrypt the input text using the RSA algorithm.
    -   *Decrypt button:* Clicking this button will decrypt the input text using the RSA algorithm.
    -   *Public Key and Private Key input fields:* These are where you should enter the public and private keys, respectively. The keys should be in the format `e,n` or `d,n`, where `e` and `d` are the exponent values and `n` is the modulus value.
2.  **To encrypt a text:**
    
    -   Enter the text you want to encrypt in the Input text field.
    -   Enter the appropriate public key in the Public Key input field.
    -   Click the Encrypt button.
    -   The encrypted text will be displayed in the Output text field.
3.  **To decrypt a text:**
    
    -   Enter the encrypted text in the Input text field.
    -   Enter the appropriate private key in the Private Key input field.
    -   Click the Decrypt button.
    -   The decrypted text will be displayed in the Output text field.


The encryption process converts the input text into ASCII values, raises each ASCII value to the power of the public key exponent (e), and takes the modulus of the result with the public key modulus (n). 
The decryption process raises each encrypted value to the power of the private key exponent (d) and takes the modulus of the result with the private key modulus (n). The decrypted ASCII values are then converted back to text.

1-) When you first open the application, you will be presented with a window similar to the following:
![1](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/gui/1.png?raw=true)

2-) enter the values for the public and private keys. First, enter the value for 'e' or 'd', and then enter the value for 'n'. (e=17 , n=3233/ d=413, n=3233)

![2](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/gui/2.png?raw=true)

3-) enter the text you want to encrypt or decrypt in the Input section. Then, depending on the operation you want to perform, click either the "Encrypt" or "Decrypt" button. (In this example, I will be using the encryption operation.)
![3](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/gui/3.png?raw=true)

4-)The encrypted message will be provided in the program's output section.

![4](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/gui/4.png?raw=true)

5-)You can perform the same steps for the decryption operation.

![5](https://github.com/Yagiz-Gur/RSA/blob/main/screenshot/gui/5.png?raw=true)