from dotenv import load_dotenv
import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

SYSTEM_PROMPT = """
You are SerenityBot, a helpful and polite hotel concierge assistant at Hotel Serenity.
You can help guests with:
- Room service
- Spa booking
- Housekeeping
- Airport pickup
- Restaurant reservations
- Wi-Fi and checkout info

Always be polite, concise, and confirm actions. Ask for clarification if needed.
"""
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# print("Hugging Face Token Loaded:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceEndpoint(
    # repo_id="google/flan-t5-large",
    # repo_id="HuggingFaceH4/zephyr-7b-beta",
    repo_id="mistral-7b-instruct-v0.1",
    # repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    temperature=0.5,
    max_new_tokens=256
)
memory = ConversationBufferMemory()

concierge_bot = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)
