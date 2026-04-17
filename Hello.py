import os
from pathlib import Path

import certifi
from dotenv import load_dotenv

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

if not AGENT_ID or not API_KEY:
    raise RuntimeError("Missing AGENT_ID or API_KEY in environment.")

user_name = "Sofiia"
schedule = "Student meeting at 10 AM, exam preparation at 12 PM, and a project deadline at 5 PM."
prompt = f"Create a schedule for tomorrow based on the following events: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationInitiationData(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)


def print_agent_response(response):
    print(f"Agent: {response}")


def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")


def print_user_transcript(transcript):
    print(f"User: {transcript}")


def main():
    conversation = Conversation(
        client,
        AGENT_ID,
        config=config,
        requires_auth=True,
        audio_interface=DefaultAudioInterface(),
        callback_agent_response=print_agent_response,
        callback_agent_response_correction=print_interrupted_response,
        callback_user_transcript=print_user_transcript,
    )

    conversation.start_session()


if __name__ == "__main__":
    main()

