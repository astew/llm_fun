
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def _create_new_script_template():
  """Returns a ChatPromptTemplate for creating a new script."""

  sys_text = """\
You are an expert {language} programmer. You have been tasked with writing a \
{language} script that meets the requirements specified by the human user. The
user will place the script in a file to run it.

You will output only the text of the script file, without any additional formatting.
"""

  human_text = """\
Write me a {language} script that meets the following requiremenst.

{user_prompt}
"""

  script_messages = [
      SystemMessagePromptTemplate.from_template(sys_text),
      HumanMessagePromptTemplate.from_template(human_text)
  ]

  return ChatPromptTemplate.from_messages(script_messages)


def _create_update_script_template():
  """Returns a ChatPromptTemplate for updating a script."""

  sys_text = """\
You are an expert {language} programmer. You have been tasked with updating a \
{language} script with the requirements specified by the human user. The user \
will place the script in a file to run it.

You will output only the text of the updated script file, without any \
additional formatting or explanation.
"""

  human_text1 = """\
The old contents of the {language} script are below:
---
{content}
"""

  ai_text1 = """How would you like to modify the {language} script?"""

  human_text2 = """{user_prompt}"""

  script_messages = [
      SystemMessagePromptTemplate.from_template(sys_text),
      HumanMessagePromptTemplate.from_template(human_text1),
      AIMessagePromptTemplate.from_template(ai_text1),
      HumanMessagePromptTemplate.from_template(human_text2)
  ]

  return ChatPromptTemplate.from_messages(script_messages)

# The following are the objects to be used when importing this module.

new_script =_create_new_script_template()

update_script = _create_update_script_template()