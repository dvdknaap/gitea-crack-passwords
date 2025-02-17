# GITEA (PBKDF2) Password Cracker

This script attempts to crack a password hashed using PBKDF2 with SHA-256 by using a dictionary attack. It takes a salt, a target hash, and a wordlist as input and iterates through the wordlist to find a matching password.

## Features
- Uses PBKDF2 with SHA-256 for hashing
- Allows specifying salt, target hash, and wordlist via command-line arguments
- Default wordlist set to `rockyou.txt` if not specified

## Requirements
- Python 3.x

## Installation
Clone this repository and install any required dependencies if necessary.

```bash
git clone https://github.com/dvdknaap/gitea-crack-passwords.git
cd gitea-crack-passwords
```

## Usage
Run the script with the following command-line arguments:

```bash
python script.py -s <salt_hex> -t <target_hash_hex> [-w <wordlist_path>]
```

### Arguments:
- `-s`, `--salt` (Required): The salt in hexadecimal format
- `-t`, `--target` (Required): The target hash in hexadecimal format
- `-w`, `--wordlist` (Optional): Path to the wordlist file (default: `/usr/share/wordlists/rockyou.txt`)

### Example:
```bash
python script.py -s 8bf3e3452b78544f8bee9400d6936d34 -t e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56 -w /usr/share/wordlists/rockyou.txt
```

If no `-w` option is provided, the script defaults to using `rockyou.txt`.

## Output
The script will iterate through the wordlist, displaying the passwords being tested. If a match is found, it will display the cracked password:

```
Checking Password 1: password123
Checking Password 2: qwerty
...

Found password: 25282528
```

If no match is found, it will output:
```
Password not found.
```
