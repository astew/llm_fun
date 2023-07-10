import os
from typer import Typer
from codecraft import CodeCraft
from config import settings
from language_map import get_language

app = Typer()

@app.command()
def process_file(filename: str, prompt: str):
  content = None
  path = os.path.join('gen', filename)
  if os.path.isfile(path):
    with open(path, 'r') as f:
      content = f.read()

  cc = CodeCraft(settings.OPENAI_API_KEY)
  response = cc.run(prompt, get_language(filename), content)

  with open(path, 'w') as f:
    print(response, file=f)

if __name__ == "__main__":
  app()
