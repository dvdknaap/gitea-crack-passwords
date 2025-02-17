import hashlib
import binascii
import argparse

def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
    hash_value = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations,
        dklen
    )
    return hash_value

def find_matching_password(dictionary_file, target_hash, salt, iterations=50000, dklen=50):
    target_hash_bytes = binascii.unhexlify(target_hash)
    
    with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
        count = 0
        for line in file:
            password = line.strip()
            hash_value = pbkdf2_hash(password, salt, iterations, dklen)
            count += 1

            print(f"Checking Password {count}: {password}")

            if hash_value == target_hash_bytes:
                print(f"\nFound password: {password}")
                return password

        print("Password not found.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PBKDF2 Password Cracker")
    parser.add_argument("-s", "--salt", required=True, help="Salt in hex format")
    parser.add_argument("-t", "--target", required=True, help="Target hash in hex format")
    parser.add_argument("-w", "--wordlist", default="/usr/share/wordlists/rockyou.txt", help="Path to wordlist file")
    
    args = parser.parse_args()
    
    salt = binascii.unhexlify(args.salt)
    target_hash = args.target
    dictionary_file = args.wordlist
    
    find_matching_password(dictionary_file, target_hash, salt)
