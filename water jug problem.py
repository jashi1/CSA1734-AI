from collections import defaultdict
v=defaultdict(lambda: False)
J1, J2, L = 0, 0, 0
def Water(X, Y):   
    global J1, J2, L
    if (X == L and Y == 0) or (Y == L and X == 0): 
        print("(",X, ", ",Y,")", sep ="") 
        return True
    if v[(X, Y)] == False: 
        print("(",X, ", ",Y,")", sep ="") 
        v[(X, Y)] = True
        return (Water(0, Y) or
                Water(X, 0) or
                Water(J1, Y) or
                Water(X, J2) or
                Water(X + min(Y, (J1-X)), 
                Y - min(Y, (J1-X))) or
                Water(X - min(X, (J2-Y)), 
                Y + min(X, (J2-Y)))) 
    else: 
        return False
J1=int(input("enter the first water jug number:"))
J2=int(input("enter the second water jug number:"))
L=int(input("enter the number of litres:"))
print("Path is as Follow:")  
Water(0, 0)
