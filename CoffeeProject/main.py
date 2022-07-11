MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO : 1. Print report
# Get the available water milk and coffee and print out
def report(resource , money_recd):
    #return resources
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    print(f"Water : {water} ml")
    print(f"Milk : {milk} ml")
    print(f"Coffee : {coffee} ml")
    print(f"Money : ${money_recd}")
    return


# TODO : 2. Check available data for coffee
def check_availability(userchoice) :
    #get the requirements
    water_req = int(MENU[userchoice]["ingredients"]["water"])
    milk_req = 0
    if (user_choice == "espresso"):
        milk_req = 0
    else:
        milk_req = int(MENU[userchoice]["ingredients"]["milk"])
    coffee_req = int(MENU[userchoice]["ingredients"]["coffee"])
    # get the available resource
    water_avail = int(resources["water"])
    milk_avail = int(resources["milk"])
    coffee_avail = int(resources["coffee"])
    cost = 0
    if (milk_avail >= milk_req) and (coffee_avail >= coffee_req) and (water_avail >= water_req) :
        cost = MENU[userchoice]["cost"]

    return cost

# TODO : 3. Make coffee
# TODO : 4. Sufficient coin?
def enough_money(qtr,dyme, nckl, cent, cost):
    total_cost = 0
    total_cost = float(qtr) * 0.25 + float(dyme) *0.10 + float(cent) * 0.01 + float(nckl) *0.05
    if (total_cost >= cost) :
        #return the money if anything extra
        return total_cost - cost
    else :
        return -1

def make_coffee(userchoice):
    #deduct all the ingresients from resources
    water_need = int(MENU[userchoice]["ingredients"]["water"])
    milk_need = 0
    if (user_choice == "espresso"):
        milk_need = 0
    else:
        milk_need = int(MENU[userchoice]["ingredients"]["milk"])
    coffee_need = int(MENU[userchoice]["ingredients"]["coffee"])
    # get the available resource
    water_avail = int(resources["water"])
    milk_avail = int(resources["milk"])
    coffee_avail = int(resources["coffee"])
    #update resources
    resources["water"] = water_avail - water_need
    resources["milk"] = milk_avail - milk_need
    resources["coffee"] = coffee_avail - coffee_need
    return


#check if machine is Off
is_machine_on = True
money_earned = 0
while is_machine_on :
        # Get the input from user
        user_choice = input("What would you like to have ? espresso/latte/cappuccino :")
        if user_choice == "report" :
            #Call function report
            report(resource = resources, money_recd= money_earned)
        elif user_choice == "off" :
            is_machine_on = False
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino" :
            #get the index of user_choice
            #check for the availability
            money_toget = check_availability(userchoice= user_choice)
            #if available
            if float(money_toget) > 0 :
                #print("available")
                #get money
                print(f"Cost of {user_choice} is $ {money_toget}")
                q = int(input("How many Quarters? : "))
                d = int(input("How many Dimes? : "))
                n = int(input("How many Nickels? : "))
                c = int(input("How many cents? : "))
                return_money = enough_money(qtr=q,dyme=d,nckl=n,cent=c,cost=money_toget)
                return_money = format(return_money,'.2f')
                #print(return_money)
                    #if money is sufficient
                if float(return_money) == -1 :
                    print ("Insufficient money")
                    #set to exit program
                else :
                    if float(return_money) == 0.00 :
                        print("Thank you for the order")
                    else:
                        print ("Thank you for the order")
                        print (f"Here is your change : ${return_money}")
                    #make coffee
                    make_coffee(userchoice= user_choice)
                    money_earned += money_toget
                    print(f"Here is your {user_choice} , Enjoy !!")
            else:
                print("Sorry not available!")
        else :
            print("Not a valid choice")