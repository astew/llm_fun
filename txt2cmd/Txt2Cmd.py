from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate

from .prompt import template, chat_template
from .prompt.output_parser import CodeOutputParser


# Use a user prompt to create or update a script
# This version uses a normal completion model
class Txt2Cmd(object):

  def __init__(self, openai_api_key = None):

    llm_kwargs = {
      "model": "text-davinci-003",
      "temperature": 0,
    }
    if openai_api_key is not None:
      llm_kwargs["openai_api_key"] = openai_api_key
    
    self.llm = OpenAI(**llm_kwargs)
      
  def new_script(self, user_prompt, language):
    prompt = template.new_script.format(user_prompt=user_prompt, language=language)
    response = self.llm.predict(prompt)
    return response.replace("```","")

  def update_script(self, user_prompt, language, content):
    prompt = template.update_script.format(user_prompt=user_prompt, language=language, content=content)
    response = self.llm.predict(prompt)
    return response.replace("```","")


# Same as CodeCraft, but uses a chat completion model
class ChatTxt2Cmd(object):

  def __init__(self, openai_api_key = None, debug = False):

    llm_kwargs = {
      "model": "gpt-3.5-turbo",
      "temperature": 0,
    }
    if openai_api_key is not None:
      llm_kwargs["openai_api_key"] = openai_api_key
    
    self.llm = ChatOpenAI(**llm_kwargs)
    self.parser = CodeOutputParser()
    self.debug = debug
      

  def new_script(self, user_prompt, language):
    prompt = chat_template.new_script.format_prompt(
        language=language,
        user_prompt=user_prompt
    ).to_messages()

    if self.debug:
      print("\n".join([x.content for x in prompt]))

    response = self.llm.predict_messages(prompt).content
    code_str = self.parser.parse(response)
    return code_str


  def update_script(self, user_prompt, language, content):
    prompt = chat_template.update_script.format_prompt(
        language=language,
        content=content,
        user_prompt=user_prompt
    ).to_messages()

    if self.debug:
      print("\n".join([x.content for x in prompt]))

    response = self.llm.predict_messages(prompt).content
    code_str = self.parser.parse(response)
    return code_str

