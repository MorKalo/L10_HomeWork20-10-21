#ייצר את הפונקציות הבאות: div, mul, sub, add
#פונקציות אלו צריכות לקבל שני פרמטרים y, x .כל אחת מהן צריכה לחשב את הפעולה המתמטית שהיא מייצגת ולהחזיר את התוצאה
#כעת קלוט שני מספרים מהמשתמש )באמצעות input ,)קרא לארבעת הפונקציות שכתבת והדפסאת מה שהן החזירו
#default ל- y, x אשר הוא אפס

#add=חיבור

def getDiv(x=0,y=0): #div=חילוק
    div=x/y
    return div

def getMul (x=0, y=0): #multiplication=כפל
    mul=x*y
    return mul

def getSub(x=0, y=0): #Subtraction=חיסור
    sub=x-y
    return sub

def getAdd(X=0, Y=0): #add=חיבור
    add=x+y
    return add
x=int(input('plz enetr a number for x: '))
y=int(input('plz enter a number for y: '))
print(f'the result of division x({x}) in y({y}) is {getDiv(x,y)}')
print(f'the result of multifunction x({x}) with y({y}) is {getMul(x,y)}')
print(f'the result of subtraction x({x}) in y({y}) is {getSub(x,y)}')
print(f'the result of add x({x}) with y({y}) is {getAdd(x,y)}')