from django.shortcuts import render
from gameboard.draw import *


def board(request):
    # build the blocks
    blocks = create_gameboard()
    return render(request, 'checkers/board.html', {'blocks': blocks})
