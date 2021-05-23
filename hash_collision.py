import hashlib
import random
import string
from cryptography.fernet import Fernet



def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')
    # Collision finding code goes here

    last_k_in_X = "1"
    last_k_in_Y = "0"
    while last_k_in_X != last_k_in_Y:
        # create string
        str1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        str2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        encoded1, encrypted1 = encode_and_encrypt(str1)
        encoded2, encrypted2 = encode_and_encrypt(str2)

        # convert to binary
        x = hex_to_binary(encrypted1, 16)
        y = hex_to_binary(encrypted2, 16)

        # cut and keep only the last k digits binary
        last_k_in_X = x[-k:]
        last_k_in_Y = y[-k:]

    return encoded1, encoded2


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
    return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)


def main():
    print(hash_collision(8))


def encode_and_encrypt(string):
    encoded = string.encode()
    result = hashlib.sha256(encoded)
    result_hex = result.hexdigest()
    return encoded, result_hex


if __name__ == "__main__":
    main()
