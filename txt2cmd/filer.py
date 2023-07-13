import logging
import os

from config import settings


def read(in_file):
    filepath = os.path.abspath(in_file)
    
    if not os.path.isfile(filepath):
        raise Exception(f"File {filepath} does not exist")
    
    with open(filepath, 'r') as f:
        return f.read()

def write(response, file=None):
    logging.debug(f"Writing response to {file}")
    if not os.path.isdir(settings.GENERATION_DIRECTORY):
        os.mkdir(settings.GENERATION_DIRECTORY)
    
    if file:
        with open(os.path.join(settings.GENERATION_DIRECTORY ,file), 'w') as f:
            print(response, file=f)
    else:
        print(response)