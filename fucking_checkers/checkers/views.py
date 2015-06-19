from django.shortcuts import render

def board(request):
    return render(request, 'checkers/board.html', {})
