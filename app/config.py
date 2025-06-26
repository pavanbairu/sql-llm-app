import os
from dotenv import load_dotenv

load_dotenv()

EURIAI_API_KEY = os.getenv("EURIAI_API_KEY")
EURIAI_API_URL = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
MODEL_NAME = "gpt-4.1-nano"
DATABASE_URI = os.getenv("DATABASE_URI")
PROMPT_FILE_PATH = os.path.join(os.getcwd(),"prompt_template.txt")

