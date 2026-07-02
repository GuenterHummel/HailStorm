import base64
import hashlib
import json
import math
import random
from typing import Dict, Tuple

def generate_salt() -> str:
    #base = random.randint(0, 2 ** 32)
    base = 567518
    # create a sha256 hash of the base
    hashed_base = hashlib.sha256(str(base).encode()).hexdigest()
    print("hashed_base =", hashed_base)
    return hashed_base

def generate_password_hash(username: str, password: str, public_key: str) -> str:
    combined_encoded = f"{username}{public_key}{password}".encode()
    print("combined_encoded =", combined_encoded)

    salted_hash = hashlib.sha256(f"{username}{public_key}{password}".encode()).digest()
    print("salted_hash =", salted_hash)

    salted_hash_hex  = hashlib.sha256(f"{username}{public_key}{password}".encode()).hexdigest()
    print("salted_hash_hex =", salted_hash_hex)

    # convert the salted hash to base64
    password_hash = base64.b64encode(salted_hash).decode()
    print("password_hash =", password_hash)
    return password_hash


def generate_password_token(salt: str, password_hash: str) -> Tuple[str, str]:
    # create a sha256 hash of the salt and password hash
    print("salt =", salt)
    print("password_hash =", password_hash)
    print("combined_input =", f"{salt}{password_hash}".encode())

    password_token = hashlib.sha256(f"{salt}{password_hash}".encode()).hexdigest()
    print("password_token =", password_token)

    return salt, password_token


def generate_auth_token(password_token: Tuple[str, str], local_timestamp) -> str:
    time_mark = str(math.floor(local_timestamp / 10))
    token_hash = hashlib.sha256(f"{time_mark}{password_token[1]}".encode()).hexdigest()
    return f"{password_token[0]}.{token_hash}"


def generate_login_token(timestamp: int, public_key: str, username: str, password: str):
    salt = generate_salt()
    password_hash = generate_password_hash(username, password, public_key)
    password_token = generate_password_token(salt, password_hash)
    auth_token = generate_auth_token(password_token, timestamp)

    print(username, password_hash, password_token, auth_token)

username = "admin"
password = "admin"
public_key = "<?xdf ax='F_A12' elm='sdF'?>"
timestamp = 47193

generate_login_token(timestamp, public_key, username, password)
