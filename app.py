from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
app = Flask(__name__)

@app.route('/')
def home():
    api_key = os.getenv('GOOGLE_API_KEY')
    return f'API Key: {api_key}'
@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
    app.run(debug=True)
