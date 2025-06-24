import os
import requests
from dotenv import load_dotenv
import chainlit as cl

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referrer": "http://localhost:8000"
}

@cl.on_chat_start
async def start():
    # Initialize chat history
    cl.user_session.set("history", [])
    await cl.Message(content="Welcome to the Chatbot!").send()

@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve and update chat history
    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": message.content})

    payload = {
        "model": model_name,
        "messages": history,
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        res = response.json()
        bot_msg = res["choices"][0]["message"]["content"]

        history.append({"role": "assistant", "content": bot_msg})
        cl.user_session.set("history", history)

        await cl.Message(content=bot_msg).send()

    except requests.exceptions.RequestException as e:
        error_msg = f"Error: {str(e)}"
        await cl.Message(content=error_msg).send()
