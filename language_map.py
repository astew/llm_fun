_langdict = {
    "py": "Python",
    "java": "Java",
    "cpp": "C++",
    "cc": "C++",
    "cxx": "C++",
    "c": "C",
    "js": "JavaScript",
    "html": "html",
    "css": "CSS",
    "rb": "Ruby",
    "php": "PHP",
    "swift": "Swift",
    "pl": "Perl",
    "go": "Go",
    "rs": "Rust",
    "sh": "Shell",
}


def get_language(filename: str) -> str:
    """Returns an assumed language based on file extension

    Args:
        filename (str): The filename to interpret

    Returns:
        str: The name of a language
    """
    if filename is None:
        return "Python"
    return _langdict.get(filename.split(".")[-1], None)
