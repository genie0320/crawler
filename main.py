import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")

'''
python -m venv genv
genv\Scripts\activate
pip install python-dotenv
python main.py
pip freeze > requirements.txt
'''