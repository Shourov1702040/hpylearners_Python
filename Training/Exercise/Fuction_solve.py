def Fuction1(a):
    S = a.replace(" ","")
    Q = S.replace(".","")
    # R = Q.isupper()
    print(Q[0], end='')
    for i in range(1,len(Q)):
        if Q[i].isupper():
            print(" ", end='')
            print(Q[i], end='')
        else:
            print(Q[i], end='')

def Fuction2(a):
    S = a.replace(" ","")
    Q = S.replace(".","")
    R = ' '

    for ch in Q:
        if ch.isupper():
            R = R+' '+ch
        else:
            R=R+ch
    R = R.lstrip()
    print(R)


Fuction2("       Toufiq...ur........     Rah...man")



# def Fuction(a):
#     S = a.replace(" ","")
#     Q = S.replace(".","")
#     return Q
# result = Fuction("       Toufiq...ur........     Rah...man")
# print(result)
# Sa = "To"
# print(Sa.isupper())