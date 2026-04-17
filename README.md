# AI_Voice_Assistant

A Python-based implementation of the ElevenLabs Conversational AI platform. This project demonstrates a low-latency voice assistant capable of dynamic context injection, interrupt handling, and secure environment management.
----------------------------------------------------
Features:
----------------------------------------------------
- real-time voice synthesis & recognition: utilizes WebSockets for fluid, duplex communication between the user and the AI agent.

- overrides agent prompts at runtime to inject user-specific data (e.g. student schedules and deadlines).

- interrupt handling: implemented callback logic to manage agent "speech corrections" when interrupted by the user, ensuring a natural conversational flow.

- secure: python-dotenv for sensitive credential isolation and certifi for production-grade SSL/TLS certificate verification
----------------------------------------------------
Tech Stack
----------------------------------------------------
Python 3.10+
API: ElevenLabs Conversational AI SDK
audio interface: PyAudio / Default Audio Interface
environment management: python-dotenv, pathlib
security: certifi (SSL Certificate Verification)
----------------------------------------------------
How it works
----------------------------------------------------
script initializes a secure connection to a pre-configured ElevenLabs Agent. It overrides the default system prompt with a dynamic schedule based context, which allows AI to act as a personalized assistant.

system uses three primary callback functions to manage the interaction:

callback_user_transcript: captures and prints real-time speech-to-text results.

callback_agent_response: handles the delivery of the AI's synthesized voice.

callback_agent_response_correction: manages the agent's logic state if a user interrupts the AI mid-sentence.
