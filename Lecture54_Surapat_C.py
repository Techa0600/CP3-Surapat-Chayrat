def login():
    username = input("Username:")
    password = input("Password:")
    if username == "admin" and password == "1234":
        return showmenu()
    else:
        return login()
def showmenu():
    print("Done!")
    print("-----Shop-----")
    print("1.vat calculator")
    print("2.price calculator")
    return menuselect()
def menuselect():
    userselected = int(input(">>"))
    if userselected == 1:
        return vatcalculate(totalprice = float(input()))
    elif userselected == 2:
        return pricecalculate()
def vatcalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def pricecalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatcalculate(price1 + price2)

print(login())