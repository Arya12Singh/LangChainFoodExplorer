import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('World Foods Explorer')
input_text = st.text_input("Enter the food item you're curious about")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['food'],
    template="Tell me about the food item {food}."
)

# Memory
food_memory = ConversationBufferMemory(input_key='food', memory_key='food_history')

## OPENAI LLMS
llm = OpenAI(temperature=0.8)
chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='origin',
    memory=food_memory
)

# Prompt for nutritional facts
second_input_prompt = PromptTemplate(
    input_variables=['food'],
    template="Provide nutritional facts for {food}."
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='nutrition',
    memory=ConversationBufferMemory(input_key='food', memory_key='nutrition_history')
)

# Prompt for recipes
third_input_prompt = PromptTemplate(
    input_variables=['food'],
    template="Can you share some recipes that use {food}?"
)

chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key='recipes',
    memory=ConversationBufferMemory(input_key='food', memory_key='recipe_history')
)

# Combine chains in a sequence
parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['food'],
    output_variables=['origin', 'nutrition', 'recipes'],
    verbose=True
)

if input_text:
    response = parent_chain({'food': input_text})
    st.write(response)

    with st.expander('Origin and History'):
        st.info(food_memory.buffer)

    with st.expander('Nutritional Facts'):
        st.info(chain2.memory.buffer)

    with st.expander('Recipes'):
        st.info(chain3.memory.buffer)
