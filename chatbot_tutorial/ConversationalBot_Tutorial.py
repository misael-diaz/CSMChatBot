# -*- coding: utf-8 -*-
"""ConversationalBot_Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HYqOH_uwzkH-Z0Quzrfz8Z61CQYEh1Yf

Tutorial on buildin simple chatbot with LangChain. Based on:

https://python.langchain.com/docs/use_cases/chatbots/
"""

# !pip install --upgrade --quiet langchain langchain-openai

## Uncomment below to instal newest versiono f langchain
# !pip install --upgrade --quiet  langchain langchain-openai

import os

# Define API key for OPenAI
# Set API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

"""With a plain chat model, we can get chat completions by passing one or more messages to the model.

"""

## Load default OpenAI chatbot
from langchain_openai import ChatOpenAI
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

from langchain_core.messages import HumanMessage, SystemMessage

# Invoke the chatbot using a hummanMessage to reecive an AIMessage
response = chat.invoke(
    [
        HumanMessage(
            content="Translate this sentence from English to French: I love programming."
        )
    ]
)

response

## Take the content from the output
print(response.content)

"""### We can assign a systemMessage, which will define the role of the chatbot.

"""

chat.invoke(
    [
        SystemMessage(
            content = ' You are a helpfull assistant that translates English to french'
        ),
        HumanMessage(
            content="I love programming and everything else"
        )
    ]
)

"""Up to this point the chatbot does not have memory. It can only respond to individual inputs whitout knowledge of previous inputs. Confirm this by asking the model what did it say before."""

chat.invoke([HumanMessage(content="What did you just say?")])

"""Adding memory will be covered in the future"""

