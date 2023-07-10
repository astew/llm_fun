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

def get_language(filename):
  return _langdict.get(filename.split('.')[-1], None)