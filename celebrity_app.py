import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Custom CSS for a sleek look
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .stTextInput, .stTextArea {
        background-color: white;
        border: 1px solid #d0d0d0;
        border-radius: 5px;
        padding: 0.5rem;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.8rem 1.5rem;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stExpander{
       border: 1px solid #d0d0d0;
       border-radius:5px;
       margin-bottom: 10px;
    }
     .stExpander > details > summary{
       background-color: #e0e0e0;
        padding: 0.5rem;
        cursor: pointer;
        border-radius:5px;
    }
     .stExpander > details > div {
       padding: 1rem;
     }
    .reportview-container .main .stAlert{
       background-color:#eaf5f9;
       border:1px solid #90e7f3;
       color:#178396;
       border-radius:5px;
       padding: 1rem;
    }
    h1 {
        color: #333;
    }
    .stInfo{
       background-color: #eaf5f9;
       border:1px solid #90e7f3;
       color:#178396;
       border-radius:5px;
       padding: 1rem;
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Celebrity Info Explorer")

with st.container():
    input_text = st.text_input("Enter a celebrity name:", placeholder="e.g., Mohammed Ali the Boxing king")


# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me some interesting facts about the celebrity {name}.",
)

second_input_prompt = PromptTemplate(
    input_variables=["person"],
    template="When was {person} born?",
)

third_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="Mention 5 major world events that happened around {dob}.",
)


# Memory
person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
descr_memory = ConversationBufferMemory(input_key="dob", memory_key="description_history")

# OPENAI LLMS
llm = OpenAI(temperature=0.8)


chain = LLMChain(
    llm=llm, prompt=first_input_prompt, verbose=True, output_key="person", memory=person_memory
)

chain2 = LLMChain(
    llm=llm, prompt=second_input_prompt, verbose=True, output_key="dob", memory=dob_memory
)

chain3 = LLMChain(
    llm=llm, prompt=third_input_prompt, verbose=True, output_key="description", memory=descr_memory
)


parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=["name"],
    output_variables=["person", "dob", "description"],
    verbose=True,
)

if input_text:
    with st.spinner("Fetching information..."):
        try:
            results = parent_chain({"name": input_text})
            
            st.markdown("### Search Results")
            
            st.write(f"**Celebrity:** {input_text}")
            st.markdown(f"**About:**\n {results['person']}")
            st.markdown(f"**Born:** \n{results['dob']}")
            st.markdown(f"**Major events:**\n {results['description']}")

            #with st.expander("Raw History - Celebrity"):
                #st.info(person_memory.buffer)

            #with st.expander("Raw History - Events"):
               #st.info(descr_memory.buffer)

        except Exception as e:
            st.error(f"An error occurred: {e}")