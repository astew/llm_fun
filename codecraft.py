from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI


class CodeCraft(object):

  def __init__(self, openai_api_key = None):
    
    if openai_api_key is not None:
      self.llm = OpenAI(model="text-davinci-003", temperature=0, openai_api_key=openai_api_key)
    else:
      self.llm = OpenAI(model="text-davinci-003", temperature=0)
      


  def new_script(self, user_prompt, language):
    prompt = f"""
  Below is a {language} script (formatted using markdown) which meets the following requirements.

  {user_prompt}

  Script:

  """
    return self.llm.predict(prompt).replace("```","")



  def update_script(self, user_prompt, language, content):
    prompt = f"""
  User request: Given the following {language} code:

  ```
  {content}
  ```

  {user_prompt}

  AI response: Here is the new script, with correct indentation, written by an expert python programmer (without any explanation):

  """
    response = self.llm.predict(prompt)
    # remove backticks if they're there
    return response.replace("```","")



  def run(self, user_prompt, language, content = None):

    if content is None:
      return self.new_script(user_prompt, language)
    else:
      return self.update_script(user_prompt, language, content)

if __name__ == '__main__':
  cc = CodeCraft()
  # print(cc.run("Requests the user to enter a file path and outputs the MD5 hash of the supplied file.", "python"))

  print(cc.run("Update this script to print a QR code of the MD5 hash.", "python", content="""
  import hashlib

file_path = input("Please enter a file path: ")

with open(file_path, 'rb') as f:
    data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
    print("The MD5 hash of the supplied file is: " + md5_hash)
    """))