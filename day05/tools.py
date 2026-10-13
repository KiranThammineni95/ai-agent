from datetime import datetime
import random  
import secrets
import string

def get_current_time():
    """Returns the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S;%p")

def roll_dice():
    """Returns a random number between 1 and 6, simulating a dice roll."""
    return random.randint(1, 6)
def generate_password(length=12):
    """Generates a secure random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
def read_text_file (file_name):
    """Reads the content of a text file and returns it as a string."""
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:   
        return f"Error: The file '{file_name}' file was not found."