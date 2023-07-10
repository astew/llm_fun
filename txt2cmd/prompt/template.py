
from langchain import PromptTemplate


new_script_text = """/
Below is a {language} script (formatted using markdown) which meets the following requirements.

{user_prompt}

Script:
"""

new_script = PromptTemplate(
    input_variables=["language", "user_prompt"],
    template=new_script_text)


update_script_text = """/
User request: Given the following {language} code:

```
{content}
```

{user_prompt}

AI response: Here is the new script, with correct indentation, written by an expert python programmer (without any explanation):
"""

update_script = PromptTemplate(
    input_variables=["language", "user_prompt", "content"],
    template=update_script_text)