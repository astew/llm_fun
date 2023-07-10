from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate

import prompt.template as template
import prompt.chat_template as chat_template

# Name was a chatGPT suggestion, rename this later

# Use a user prompt to create or update a script
# This version uses a normal completion model
class CodeCraft(object):

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
class ChatCodeCraft(object):

  def __init__(self, openai_api_key = None):

    llm_kwargs = {
      "model": "gpt-3.5-turbo",
      "temperature": 0,
    }
    if openai_api_key is not None:
      llm_kwargs["openai_api_key"] = openai_api_key
    
    self.llm = ChatOpenAI(**llm_kwargs)
      

  def new_script(self, user_prompt, language):
    prompt = chat_template.new_script.format_prompt(
        language=language,
        user_prompt=user_prompt
    ).to_messages()

    response = self.llm.predict_messages(prompt)
    return response


  def update_script(self, user_prompt, language, content):
    prompt = chat_template.update_script.format_prompt(
        language=language,
        content=content,
        user_prompt=user_prompt
    ).to_messages()

    response = self.llm.predict_messages(prompt)
    return response

