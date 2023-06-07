class ASCIICodeConverter:
    
    def to_ascii(text):
        """
        Converts the given text character by character to ASCII codes.

        Parameters:
            text (str): The text to be converted to ASCII codes.

        Returns:
            list: A list containing the ASCII codes of the text.
        """
        ascii_values = []
        for i in text:
            ascii_values.append(ord(i))
        
        return ascii_values
    
   
    def from_ascii(ascii_codes): 
        """
        Converts the given list of ASCII codes to text.

        Parameters:
            ascii_codes (list): A list of ASCII codes to be converted to text.

        Returns:
            str: The text representation of the ASCII codes.
        """
        text = []
        for i in ascii_codes:
            text.append(chr(i))

        text_values = "".join(text)
        return text_values


class RSAEncryptor:
    
    def encrypt(x, e, n):
        """
        Performs encryption on a list of values using the RSA algorithm.

        Parameters:
            x (list): The list of values to be encrypted.
            e (int): The public exponent used for encryption.
            n (int): The modulus used for encryption.

        Returns:
            list: The encrypted values obtained by applying the RSA algorithm.
        """
        output = []
        for i in x:
            output.append((i ** e) % n)
        return output
    
    
    def decrypt(x, d, n):
        """
        Performs decryption on a list of encrypted values using the RSA algorithm.

        Parameters:
            x (list): The list of encrypted values to be decrypted.
            d (int): The private exponent used for decryption.
            n (int): The modulus used for decryption.

        Returns:
            list: The decrypted values obtained by applying the RSA algorithm.
        """
        output = []
        for i in x:
            output.append((i ** d) % n)
        return output


while True:
    try:
        selection = int(input("-*-*-*-*-*-*-*-*-\n1-) Encryption\n2-) Decryption\n0-) Exit\nSelect: "))
        if selection == 1:
            text = input("Enter the text you want encrypted: ")
            ascii_text = ASCIICodeConverter.to_ascii(text)
            e = int(input("Enter public key's e: "))
            n = int(input("Enter public key's n: "))
            encrypted_text = RSAEncryptor.encrypt(ascii_text, e, n)
            print(encrypted_text)
              
        elif selection == 2:
            encrypted_text = input("Enter the text you want decrypted: ").split(", ")
            encrypted_text = [int(i) for i in encrypted_text]
            d = int(input("Enter private key's d: "))
            n = int(input("Enter private key's n: "))
            decrypted_text = RSAEncryptor.decrypt(encrypted_text, d, n)
            text = ASCIICodeConverter.from_ascii(decrypted_text)
            print(text)
        elif selection ==0:
            break
            
        else:
            print("\nInvalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print("An error occurred:", str(e))