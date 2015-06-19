from django.shortcuts import render


def is_odd(n):
    if not n % 2 == 0:
        return True
    return False

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def board(request):
    # build the blocks
    blocks = []
    for i in range(0, 64):
        print "NUM %s" % i
        offset = int(0)
        if i >= 8 and i < 16:
            print "\t- offset!"
            offset = -1
        if i >= 24 and i < 32:
            print "\t - offset!"
            offset = -1
        if i >= 40 and i < 48:
            print "\t - offset!"
            offset = -1
        if i >= 56 and i < 64:
            print "\t - offset!"
            offset = -1

        css_class = "even"
        if is_odd(i + offset):
            css_class = "odd"
        blocks.append({'class': css_class, 'num': i})
    return render(request, 'checkers/board.html', {'blocks': blocks})
