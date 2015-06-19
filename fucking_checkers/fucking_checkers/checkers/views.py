from django.shortcuts import render

def board(request):
    return render('checkers/board.html', {})
