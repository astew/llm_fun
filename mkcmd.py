import os
import typer
from typer import Typer, Option
from codecraft import CodeCraft, ChatCodeCraft
from config import settings
from language_map import get_language

app = Typer()

@app.command()
def new(filename: str, prompt: str, dry_run: bool = Option(False, "--dry", help="Prints result instead of writing to file.")):
  content = None
  
  filepath = os.path.abspath(filename)
  
  if not dry_run and os.path.isfile(filepath):
    raise Exception(f"File {filepath} already exists")

  cc = ChatCodeCraft(settings.OPENAI_API_KEY)
  response = cc.new_script(prompt, get_language(filename))

  if dry_run:
    print(response)
    return

  os.makedirs(os.path.dirname(filepath), exist_ok=True)
  with open(filepath, 'w') as f:
    print(response, file=f)
    

@app.command()
def update(filename: str, prompt: str, dry_run: bool = Option(False, "--dry", help="Prints result instead of writing to file.")):
  content = None
  
  filepath = os.path.abspath(filename)
  
  if not os.path.isfile(filepath):
    raise Exception(f"File {filepath} does not exist")
  
  with open(filepath, 'r') as f:
    content = f.read()

  cc = ChatCodeCraft(settings.OPENAI_API_KEY)
  response = cc.update_script(prompt, get_language(filename), content)

  if dry_run:
    print(response)
    return

  with open(filepath, 'w') as f:
    print(response, file=f)

if __name__ == "__main__":
  app()
