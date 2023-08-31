print("OATSHOP")
username = input("USERNAME: ")
password = input("PASSWORD: ")
if username == "oat" and password == "1669":
    print("WELCOME TO OATSHOP")
    print("เลือกรายการสินค้า")
    print("1.iPhone 14 Pro Max 44,900 BAHT");print("2.iPhone 14 Pro 41,900 BAHT");print("3.iPhone 13 29,900 BAHT");print("4.iPhone 13 mini 24,900 BAHT")
    selected = int(input("หมายเลขสินค้าที่ต้องการ: "))
    quantity = int(input("จำนวนเครื่องที่ต้องการ:"))
    if selected == 1:
        print("ราคาที่ต้องชำระ iPhone 14 Pro Max",quantity,"เครื่อง","   ",quantity*44900,"BAHT")
    elif selected == 2:
        print("ราคาที่ต้องชำระ iPhone 14 ",quantity,"เครื่อง","   ",quantity*41900,"BAHT")
    elif selected == 3:
        print("ราคาที่ต้องชำระ iPhone 13 ",quantity,"เครื่อง","   ",quantity*29900,"BAHT")
    elif selected == 1:
        print("ราคาที่ต้องชำระ iPhone 13 mini",quantity,"เครื่อง","   ",quantity*24900,"BAHT")
else:
    print("username or passeord was wrong!!")
