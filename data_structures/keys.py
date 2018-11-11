import os, ecdsa, hashlib

from block import hash_SHA


def generate_private_key():
    """
    Creates a random 32 byte string used as a private key

    :no param:
    :return:    A randomly generated 32 byte string using urandom()
    """
    return os.urandom(32)

def generate_public_key(private_key):
    """
    Takes private key and puts it through the ellipical curve for public key encryption
    
    :param: private key is the randomly generated 32 byte string 
    :return:  verifying key, which effectively is the public key  
    """
    signing_key = ecdsa.SigningKey.from_string(private_key, curve = ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    return verifying_key.to_string()


 
