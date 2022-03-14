# Basic chatbot using chattero
from chattero import (
    ChatBot, BasicTransformer, BasicDataStore
)

# Stores all our words and sentences
store = BasicDataStore(
    export_to="responses.cache",
    export_after=5,
    load_from="responses.cache",
    config={
        "skip_if_file_not_found": True
    }
)

chatbot = ChatBot(
    data_store=store,
    # Handles our responses
    transformer=BasicTransformer(
        generate_sentences=True
    ),
    config={
        "chatbot_name": "Chattero"
    }
)

while True:
    sentence = input("> ")
    response = chatbot.get_response(sentence)

    print(response)
