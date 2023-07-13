import logging

from typer import Option, Typer

from language_map import get_language
from txt2cmd.filer import read, write
from txt2cmd.Txt2Cmd import ChatTxt2Cmd

app = Typer()


@app.command()
def new(
    prompt: str,
    out_file: str = Option(None, "--out-file", help="File to write the result to."),
    log_level: str = Option("INFO", "--log-level", help="The level of logger output."),
) -> None:
    """Generate a new script based on a given prompt

    Args:
        prompt (str): User defined prompt for script contents
        out_file (str, optional): Filename to write script contents. Defaults to None.
        log_level (str, optional): Output log level. Defaults to "INFO".
    """
    logging.basicConfig(level=log_level)
    cc = ChatTxt2Cmd()
    response = cc.generate_script(prompt, get_language(out_file))
    write(response, file=out_file)


@app.command()
def update(
    in_file: str,
    prompt: str,
    out_file: str = Option(None, "--out-file", help="File to write the result to."),
    log_level: str = Option("INFO", "--log-level", help="The level of logger output."),
) -> None:
    """Update a given script based on user prompt

    Args:
        in_file (str): Filename of script to update
        prompt (str): User defined prompt for script contents
        out_file (str, optional): Filename to write script contents. Defaults to None.
        log_level (str, optional): Output log level. Defaults to "INFO".
    """
    logging.basicConfig(level=log_level)
    content = read(in_file)
    cc = ChatTxt2Cmd()
    response = cc.generate_script(prompt, get_language(in_file), content)
    write(response, file=out_file)


if __name__ == "__main__":
    app()
