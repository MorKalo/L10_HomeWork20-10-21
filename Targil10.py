#כתוב פונקציה בשם getInRange אשר מקבלת שני פרמטרים: max, min
#הפונקציה אמורה לקלוט מספר מהמשתמש בלולאה, עד אשר המספר שייקלט יהיה בטווח שנשלח.
#אחרי שהפונקציה קיבלה קלט "חוקי" היא מחזירה )באמצעות return )את המספר "החוקי" שהמשתמש הקליד

#קצת הסתבכתי עם התרגיל...

def getInRange(num, _min, _max):
    while true:
        if (num>=_min) and (num<=_max):
            validnum=num
            return validnum
        else:
            num=int(input('plz enter a new num: '))


num=int(input('plz enter a num: '))
_min=int(input('plz enter a MINIMUM num: '))
_max=int(input('plz enter a MAXIMUM num: '))

print(getInRange(num, _min, _max))

