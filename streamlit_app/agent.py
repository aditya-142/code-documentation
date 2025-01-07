import openai
import os
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.code_interpreter.base import CodeInterpreterToolSpec
import streamlit as st

def return_agent(key):
    key = st.secrets['OPENAI_API_KEY']
    openai.api_key = key

    code_spec = CodeInterpreterToolSpec()
    tools = code_spec.to_tool_list()
    agent = OpenAIAgent.from_tools(
        tools,
        llm=OpenAI(temperature=0, model="gpt-4o-mini"),
        verbose=True
    )
    return agent


