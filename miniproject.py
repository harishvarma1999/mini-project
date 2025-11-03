from datetime import datetime
name=input("enter your name: ")
#list of items
lists='''
rice rs 50/kg
sugar Rs 40/kg
oil Rs 100/kg
maida Rs 40/kg
salt Rs 20/kg
jaggery Rs 50/kg
ghee Rs 1000/kg
greengram Rs 120/kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
# rate for items
items={"rice":50,"sugar":40 ,
       "oil":100,"maida":40,
       "salt":20,"jaggery":50,
       "ghee":1000,"greengram":120}
option=int(input("for items list press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    opt1=int(input("if you want to buy press 1 or press 2 for exit: "))
    if opt1==2:
        break 
    if opt1==1:
        item=input("enter your item : ")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item) 
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
                print("sorry your item is not available")
    else:
            print(" you entered  wrong number")
    inp2=(input("can i bill items yes or no: "))
    if inp2=="yes":
        pass
    if finalamount!=0:
        print(25*"=","harish supermarket",25*"=")
        print(28*"=","garividi")
        print("name:",name,30*"","date:",datetime.now())
        print(75*"-")
        print("sno",8*" ","items",8*" ","quantity",2*" ","price")
        for i in range(len(pricelist)):
            print(i,8*" ",5*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print("gst amount",40*" ",gst)
            print(75*"-")
            print(50*" ","finalamount:","Rs",finalamount)
            print(75*"-")
            print(20*" ","thank you vist again",20*" ")
            print(75*"-")