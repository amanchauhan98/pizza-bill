import time

print("|-----------------------------|")
print("       AMAN PIZZA STORE           ")
print("|-----------------------------|")
print("Welcome to Our store\n")
print("|----------------------------------------------------|")
name = str(input("Enter your name here\n"))
contact = (input("Enter your Mobile number here\n"))
address = str(input("Enter your address here\n"))
print("|----------------------------------------------------|")
print(f"Thank you Mr./Ms. {name} for entering Your Personal information.")
print("We have so many varities in our pizza store, like: Cheese Pizza , Corn Pizza , Cheese Capsicum Pizza , Extra Cheese Pizza etc...\n ")
varity = str(input("Enter the Type Of Pizza you want\n"))
if varity == "cheese pizza" or varity == "Cheese Pizza" or varity == "CHEESE PIZZA" :
    print(f"{name} you want {varity} Pizza!")
    quantity = int(input("How Much Do you want Cheese Pizza\n"))
    cost = 250
    gst = 8 * 250/100
    prize = quantity*cost + gst
    print(f"{name} your {varity} pizza of {quantity} Quantity price is {prize}")
elif varity == "corn pizza" or varity == "Corn Pizza" or varity == "CORN PIZZA" :
    print(f"{name} you want {varity} Pizza!")
    quantity = int((input("How Much Do you want Corn Pizza\n")))
    cost = 300
    gst = 8 * 300/100
    prize = quantity*cost + gst
    print(f"{name} your {varity} pizza of {quantity} Quantity price is {prize}")
elif varity == "cheese capsicum pizza" or varity == "Cheese Capsicum Pizza" or varity == "CHEESE CAPSICUM PIZZA" :
    print(f"{name} you want {varity}")
    quantity = int(input("How Much Do you want Cheese capsicum Pizza\n"))
    cost = 450
    gst = 8 * 450/100
    prize = quantity*cost + gst
    print(f"{name} your {varity} pizza of {quantity} Quantity price is {prize}")
elif varity == "extra cheese pizza" or varity == "Extra Cheese Pizza" or varity == "EXTRA CHEESE PIZZA" :
    print(f"{name} you want {varity} Pizza!")
    quantity = int(input("How Much Do you want Extra Cheese Pizza\n"))
    cost = 500
    gst = 8 * 500/100
    prize = quantity*cost + gst
    print(f"{name} your {varity} pizza of {quantity} Quantity price is {prize}")
else :
    print(f"ERROR!! Sorry {name}, But Your Input is Wrong, Please Check it Again please. Thank you!")
time.sleep(2)


def bill () :
    print("|-----------------------------|")
    print("       AMAN PIZZA STORE           ")
    print("|-----------------------------|")
    print("Name = ",name)
    print("Phone = ",contact)
    print("Address = ",address)
    print("Varity = ",varity)
    print("Quantity = ",quantity)
    print("Cost = ",cost)
    print("GST = ",gst)
    print("Price = ",prize)
    print(f"|Thank you! Mr./Ms. {name}. Have a Good day!|")
    print("|-----------------------------|")


bill()

with open("pizza bill.txt","a") as f :
    f.write(name)
    print("\n")
    f.write(contact)
    print("\n")
    f.write(address)
    print("\n")
    f.write(varity)
    print("\n")
    











