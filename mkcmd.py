import os
import typer
from typer import Typer, Option
from txt2cmd.Txt2Cmd import ChatTxt2Cmd
from config import settings
from language_map import get_language

app = Typer()

@app.command()
def new(prompt: str, out_file: str = Option(None, "--out-file", help="File to write the result to.")):
    content = None
    
    cc = ChatTxt2Cmd(settings.OPENAI_API_KEY)
    response = cc.new_script(prompt, get_language(out_file))

    if out_file:
        with open(out_file, 'w') as f:
            print(response, file=f)
    else:
        print(response)
    

@app.command()
def update(in_file: str, prompt: str, out_file: str = Option(None, "--out-file", help="File to write the result to.")):
    content = None
    
    filepath = os.path.abspath(in_file)
    
    if not os.path.isfile(filepath):
        raise Exception(f"File {filepath} does not exist")
    
    with open(filepath, 'r') as f:
        content = f.read()

    cc = ChatTxt2Cmd(settings.OPENAI_API_KEY)
    response = cc.update_script(prompt, get_language(in_file), content)

    if out_file:
        with open(out_file, 'w') as f:
            print(response, file=f)
    else:
        print(response)

if __name__ == "__main__":
    app()
