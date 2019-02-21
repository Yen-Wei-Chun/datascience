def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print('+ - - - -', end=' ')

def print_coloumn():
    print('|        ', end=' ')

def print_rows():
    do_twice(print_row)
    print('+')

def print_coloumns():
    do_twice(print_coloumn)w
    print('|')

def print_lines():
    print_rows()
    do_four(print_coloumns)

def print_grid():
    do_twice(print_lines)
    print_rows()

print_grid()
