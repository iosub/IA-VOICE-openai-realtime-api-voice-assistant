import os
from dotenv import load_dotenv

# Load environment variables from .env filekkkkk
load_dotenv()

# Access the environment variable
my_secret = os.getenv('MY_SECRET')
print(f'My secret is: {my_secret}')