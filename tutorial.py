def variabledeclarationwithoutparaameters():
    x = "shreya"
    y = 7
    print("Hello I am " + x + " and my lucky number is " + str(y))


def variabledeclaration(name, luckyno):
    print("Hello I am " + name + " and my lucky number is " + str(luckyno))


def variabledeclaration1():
    array = (10, 20, 30, 'sim', 'mobile')
    x = array[0]
    y = array[1]
    print(x, y)


def variabledeclarationparameters(index):
    array = (10, 20, 30, 'sim', 'mobile')
    x = array[index]

    print("Parameter" + str(x))


def variabledeclarationdictionary():
    dict = {"father": "kamlakar", "mother": "Maya", "sister": "Ashu"}

    print(dict)


def variabledeclarationdictionarypara(relation):
    dict = {"father": "kamlakar", "mother": "Maya", "sister": "Ashu"}
    value = dict[relation]
    print(relation + "==" + value)
    if relation == "mother":
        print(value + "== supermom")
    elif relation == "father":
        print(value + "== cool")
    else:
        print(value + "== sis")


def variabledeclarationgreater(number):
    if number > 10:
        print("given number " + str(number) + " is greater than 10")
    elif number < 10:
        print("given number " + str(number) + " is less than 10")
    else:
        print("Given Number %d is == to '10'" % number)


def variabledeclarationadd(x, y):
    add = x + y
    print("addition is " + str(add))
    print("addition is  %d " % add)
    print("sum of %d,%d is %d" % (x, y, add))


def variabledeclarationoperators(x, y, operator):
    if operator == "add":
        result = x + y
        print("sum of %d,%d is %d" % (x, y, result))
    elif operator == "sub":
        result = x - y
        print("sub of %d,%d is %d" % (x, y, result))
    else:
        print("do nothing")


def arraycontentdisplay():
    array = ["apple", "mango", "papaya", "grapes"]
    for y in array:
        print(y)


def arraycontentdisplay1(array):
    for y in array:
        if y=="aple":
            print("found")
            break
        else:
            print("not found")



arraycontentdisplay1(["gggh", "hdhd", "aple"])

arraycontentdisplay()
variabledeclarationoperators(5, 7, "add")
variabledeclarationoperators(7, 5, "sub")
variabledeclarationoperators(7, 5, "mult                                                          "
                                   ".")
variabledeclarationadd(5, 7)
variabledeclarationgreater(10)
variabledeclarationdictionarypara("sister")
variabledeclarationdictionarypara("mother")

variabledeclarationdictionary()

variabledeclarationparameters(2)
variabledeclaration1()
variabledeclaration("saurabh", 9)
variabledeclarationwithoutparaameters()
