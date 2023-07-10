from typing import List
import re

from langchain.schema import BaseOutputParser, OutputParserException

code_regex = re.compile(r"\n?```[a-zA-z0-9]*\n(.+?)\n```", re.DOTALL)


class CodeOutputParser(BaseOutputParser[str]):

  def get_format_instructions(self) -> str:
    return f"Write only a single markdown code block containing the requeated code, without any additional formatting, commentary or explanation."

  def parse(self, response: str) -> str:
    try:
      match = code_regex.match(response)
      if match is None: raise ValueError("Response does not match regex.")

      return match.group(1)

    except ValueError as e:
      raise OutputParserException(
          f"Could not parse response: {response}"
      ) from e

    @property
    def _type(self) -> str:
      return "str"


# TEST = """
# ```python
# import curses
# import time

# def main(stdscr):
#     # Set up the screen
#     curses.initscr()
#     curses.curs_set(0)
#     sh, sw = stdscr.getmaxyx()
#     w = curses.newwin(sh, sw, 0, 0)
#     w.keypad(1)
#     w.timeout(100)

#     # Initialize the snake position and direction   
#     snake_x = sw//4
#     snake_y = sh//2
#     snake = [
#         [snake_y, snake_x],
#         [snake_y, snake_x-1],
#         [snake_y, snake_x-2]
#     ]

#     # Initialize the food position
#     food = [sh//2, sw//2]
#     w.addch(food[0], food[1], curses.ACS_PI)        

#     # Initialize the score
#     score = 0

#     # Initialize the direction
#     key = curses.KEY_RIGHT

#     # Game loop
#     while True:
#         next_key = w.getch()
#         key = key if next_key == -1 else next_key   

#         # Check if the snake hits the wall or itself
#         if (
#             snake[0][0] in [0, sh] or
#             snake[0][1] in [0, sw] or
#             snake[0] in snake[1:]
#         ):
#             curses.endwin()
#             quit()

#         # Calculate the new head position
#         new_head = [snake[0][0], snake[0][1]]

#         if key == curses.KEY_DOWN:
#             new_head[0] += 1
#         if key == curses.KEY_UP:
#             new_head[0] -= 1
#         if key == curses.KEY_LEFT:
#             new_head[1] -= 1
#         if key == curses.KEY_RIGHT:
#             new_head[1] += 1

#         # Insert the new head position
#         snake.insert(0, new_head)

#         # Check if the snake eats the food
#         if snake[0] == food:
#             score += 1
#             food = None
#             while food is None:
#                 nf = [
#                     random.randint(1, sh-1),
#                     random.randint(1, sw-1)
#                 ]
#                 food = nf if nf not in snake else None
#             w.addch(food[0], food[1], curses.ACS_PI)
#         else:
#             tail = snake.pop()
#             w.addch(tail[0], tail[1], ' ')

#         # Draw the snake
#         w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
# ```
# """

# match = code_regex.match(TEST)

# if match is None: print("DIDN'T MATCH")
# else: print(match.group(1))