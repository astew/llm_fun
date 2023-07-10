from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate

import prompt.template as template

# Name was a chatGPT suggestion

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
    pt = PromptTemplate.from_template(template.new_script)
    prompt = pt.format(user_prompt=user_prompt, language=language)
    response = self.llm.predict(prompt)
    return response.replace("```","")

  def update_script(self, user_prompt, language, content):
    pt = PromptTemplate.from_template(template.update_script)
    prompt = pt.format(user_prompt=user_prompt, language=language, content=content)
    response = self.llm.predict(prompt)
    return response.replace("```","")

  def run(self, user_prompt, language, content = None):
    if content is None:
      return self.new_script(user_prompt, language)
    else:
      return self.update_script(user_prompt, language, content)
