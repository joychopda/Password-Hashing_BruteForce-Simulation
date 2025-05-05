import bcrypt
import argparse
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

# Hash a password
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    logging.info("Password hashed successfully.")
    return hashed

# Check a password against a stored hash
def check_password(stored_password: bytes, provided_password: str) -> bool:
    result = bcrypt.checkpw(provided_password.encode(), stored_password)
    logging.info(f"Password validation result: {'Success' if result else 'Failure'}")
    return result

# Simulate a dictionary brute-force attack
def brute_force(password_hash: bytes, password_list: list) -> str:
    logging.info("Starting brute-force attack simulation...")
    for password in password_list:
        time.sleep(0.5)  # Simulate delay between attempts
        logging.debug(f"Trying password: {password}")
        if check_password(password_hash, password):
            logging.info(f"Password found: {password}")
            return password
    logging.warning("Password not found in provided dictionary.")
    return None

# Main CLI logic
def main():
    parser = argparse.ArgumentParser(description="Password Hashing & Brute-force Simulator")
    parser.add_argument("password", help="Password to hash and validate")
    parser.add_argument("--brute", action="store_true", help="Simulate a brute-force dictionary attack")

    args = parser.parse_args()
    password_to_hash = args.password
    hashed = hash_password(password_to_hash)

    # Simulate validation
    check_password(hashed, password_to_hash)

    # Optional brute-force test
    if args.brute:
        dictionary = ['password', '123456', 'admin', 'welcome', 'letmein']
        found = brute_force(hashed, dictionary)
        print(f"Brute-force result: {'Password found: ' + found if found else 'Password not found'}")

if __name__ == "__main__":
    main()
