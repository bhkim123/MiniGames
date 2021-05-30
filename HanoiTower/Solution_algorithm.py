a = "1st" #tower
b = "2nd"
c = "3rd"
no = 4 #number of disc

def sol(no_disc, a, c, b):
    if no_disc == 1:
        print("Move from %s to %s" %(a, c))
        return
    sol(no_disc - 1, a, b, c)
    print("Move from %s to %s" %(a, c))
    sol(no_disc - 1, b, c, a)
    return

sol(no, a, c, b)