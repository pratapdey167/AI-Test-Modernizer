import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
BASE_URL = os.getenv("CAPGEMINI_GENAI_ENDPOINT")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError(
        "Missing Capgemini Generative Engine configuration. "
        "Set CAPGEMINI_GENAI_API_KEY and CAPGEMINI_GENAI_ENDPOINT in your .env file."
    )

llm = ChatGoogleGenerativeAI(
model=MODEL,
google_api_key=API_KEY,
temperature=0
)