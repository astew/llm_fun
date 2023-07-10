import os
from typer import Typer
from codecraft import CodeCraft
from config import settings
from language_map import get_language

app = Typer()

@app.command()
def new(filename: str, prompt: str):
  content = None
  
  filepath = os.path.abspath(filename)
  
  if os.path.isfile(filepath):
    raise Exception(f"File {filepath} already exists")

  cc = CodeCraft(settings.OPENAI_API_KEY)
  response = cc.new_script(prompt, get_language(filename))

  os.makedirs(os.path.dirname(filepath), exist_ok=True)
  with open(filepath, 'w') as f:
    print(response, file=f)
    

@app.command()
def update(filename: str, prompt: str):
  content = None
  
  filepath = os.path.abspath(filename)
  
  if not os.path.isfile(filepath):
    raise Exception(f"File {filepath} does not exist")
  
  with open(filepath, 'r') as f:
    content = f.read()

  cc = CodeCraft(settings.OPENAI_API_KEY)
  response = cc.update_script(prompt, get_language(filename), content)

  with open(filepath, 'w') as f:
    print(response, file=f)

if __name__ == "__main__":
  app()
