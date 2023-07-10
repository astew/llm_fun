
import typer
import hashlib

app = typer.Typer()

@app.command()
def hash_file(file: typer.FileText):
    """
    Calculate the MD5 hash of a file.
    """
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    typer.echo(f"MD5 hash of {file}: {md5.hexdigest()}")

if __name__ == "__main__":
    app()