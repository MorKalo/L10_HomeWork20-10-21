#כתוב פונקציה המקבלת שלושה מספרים ומחזירה את הקטן מביניהם
def getLittleNum (x, y, z):
    if x>y:
        if y>z:
            little=z
        else:
            little=y
    elif x>z:
        little=z
    else:
        little=x
    return little


x=int(input('plz enter a number for X: '))
y=int(input('plz enter a number for Y: '))
z=int(input('plz enter a number for Z: '))
print(f'the LITTLE number from the follow numbers:{x},{y},{z} is: {getLittleNum(x,y,z)}')
