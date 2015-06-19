"""
This file is responsible for generating a data structure that
will be used to draw out the checkers board in a template engine
by doing something similar to:

      <!-- stuff here -->
      <div style="width:800px;">
      {% for i in blocks %}
        <div class="block block_{{i.class}}">
          {{forloop.counter}}
        </div>
      {% endfor %}
    </div>

The checkers gameboard is a 8x8 board.

The first 8 blocks in the first row are in a red/black pattern.
After the 8th block, it will repeat the last color used
and start the pattern again for 8 more blocks, then
repeat the last color used again and proceed with the pattern
from that position.

Example (R = red, B = black:

1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16|
R | B | R | B | R | B | R | B | B | R | B | R | B | R | B | R |

If the current row is an even number, it will apply an offset of 1,
meaning every 'block' number will be deducted by 1, and then checked
if it is even or odd to apply the correct red or black color to it.
"""
from game_settings import GameSettings 
settings = GameSettings()


def create_gameboard():
    """
    Create the fucking gameboard grid!
    """
    blocks = []
    per_row = settings.per_row
    row = 1
    row_counter = 1

    for block_number in range(1, (settings.per_row ** 2) + 1):

        # check if row # is even
        offset = 0
        if row % 2 == 0:
            offset = -1

        # now determine if it is odd or even
        odd_or_even = "odd"
        if (block_number + offset) % 2 == 0:
            odd_or_even = "even"

        color = "red"
        if odd_or_even == "even":
            color = "black"
        blocks.append({'color': color, 'number': block_number, 'offset': offset})

        # if it passes the row counter, reset the row counter and +1 the row
        if row_counter == 8:
            row += 1
            row_counter = 1
        else:
            row_counter += 1
    return blocks


