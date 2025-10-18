print("\t#--WELCOME TO GOVIND'S RESTAURANT--#")
menu = {
    1:{"name":"Cheese Volcano Peppy Paneer","price": 350},
    2:{"name":"double cheese","price": 500},
    3:{"name":"chicken tikka","price": 250},
    4:{"name":"veggie","price": 350},
    5:{"name":"sweet corn","price": 450},
    6:{"name":"farmhouse pizza","price": 300}
}
cart=[]
total=0
pay=1

def place_order():

    global total
    global pay
    l=0
    print("\n")
    for i in range (1,7):
        print(f"{i}.{menu[i]["name"]} Rs.{menu[i]["price"]}")
    while True:
        choice=int(input("\nEnter between 1-6 to order: "))
        print("\nEnter 7 for exit")
        if choice==7:
            break
        else:
            l+=1
            cart.append(menu[choice]["name"])
            total+=menu[choice]["price"]
            pay=total+(15*l)
            
    main()        
    
def view_cart():
    if not cart:
        print("\nyour cart is empty\n")
        main()
    else:
        print("\nItems Total    \tRs.",total)
        print("\nTaxes& Chargers  \tRs.15")
        print("\nTo Pay       \tRs.",pay)
    main()
    
def complete_order():
    d=int(input("1. home delivery\n2. dine in\n3.takeaway "))
    if d==1:
        pay2=pay+20
        #pay+=20
        print("\nItems Total       \tRs.",total)
        print("Taxes& Chargers   \tRs.15+20(delivery charges)")
        print("To Pay            \tRs.",pay2)
    else :
        print("\nyour cart is : ",cart)
        print("\ntotal cost :",pay2)
    print("\nThank you for ordering!\nyour order is placed.")
def exit():
    print("\nThank you for Visiting!....")
    
#def coupon

def main():
    print("\n[1] View Menu\n[2]order Pizza\n[3] View cart\n[4] Complete order\n[5] Exit")
    n=(input("choose between 1-5: "))
    if n=="1":
        print("|--menu--|\n")
        for i in range (1,7):
            print(f"{i}.{menu[i]["name"]} \n\tRs.{menu[i]["price"]}")
        main()
    elif n=="2":
        place_order()
    elif n=="3":
        view_cart()
    elif n=="4":
        complete_order()
    elif n=="5":
        exit()
main()