def my_func(x1,x2,x3):
    if type(x1) == int or type(x2) == int or type(x3) == int :
        print("“Error: parameters should be float”")
    elif type(x1) != float or type(x2) != float or type(x3) != float :
        print("none")
    else:
        denom = x1+x2+x3
        if denom == 0:
            print("Not a number – denominator equals zero")
        else:
            ans = (denom*(x2+x3)*x3)/denom
            print(ans)

my_func(2.0,5.0,-7.5)