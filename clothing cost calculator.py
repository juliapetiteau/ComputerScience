#Clothing Cost Calculator


fabricnumber = int(input("How many fabrics are you using? You may enter up to 4 fabric choices"))

while True:

    def fabric_cost(fabricnumber):
        if fabricnumber == "1":
            yard_need_one= input("Number of yards of Fabric 1 needed: ")
            fabric_cost_one= input("Cost of Fabric 1 per yard: ")
            fabriccost= float(fabric_cost_one )* float(yard_need_one)

        elif fabricnumber == "2":
            yard_need_one = input("Number of yards of Fabric 1 needed: ")
            fabric_cost_one= input("Cost of Fabric 1 per yard: ")
            yard_need_two = input("Number of yards of Fabric 2 needed: ")
            fabric_cost_two= input("Cost of Fabric 2 per yard: ")
            fabric_cost= (float(fabric_cost_one )* float(yard_need_one)) + (float(fabric_cost_two)* float(yard_need_two))

        elif fabricnumber == "3":
            yard_need_one = input("Number of yards of Fabric 1 needed: ")
            fabric_cost_one= input("Cost of Fabric 1 per yard: ")
            yard_need_two = input("Number of yards of Fabric 2 needed: ")
            fabric_cost_two= input("Cost of Fabric 2 per yard: ")
            yard_need_three = input("Number of yards of Fabric 3 needed: ")
            fabric_cost_three= input("Cost of Fabric 3 per yard: ")
            fabric_cost= (float(fabric_cost_one )* float(yard_need_one)) + (float(fabric_cost_two)* float(yard_need_two)) + (float(fabric_cost_three)* float(yard_need_three))

        elif fabricnumber == "4":
            yard_need_one = input("Number of yards of Fabric 1 needed: ")
            fabric_cost_one= input("Cost of Fabric 1 per yard: ")
            yard_need_two = input("Number of yards of Fabric 2 needed: ")
            fabric_cost_two= input("Cost of Fabric 2 per yard: ")
            yard_need_three = input("Number of yards of Fabric 3 needed: ")
            fabric_cost_three= input("Cost of Fabric 3 per yard: ")
            yard_need_four = input("Number of yards of Fabric 4 needed: ")
            fabric_cost_four= input("Cost of Fabric 4 per yard: ")
            fabric_cost= (float(fabric_cost_one )* float(yard_need_one)) + (float(fabric_cost_two)* float(yard_need_two)) + (float(fabric_cost_three)* float(yard_need_three)) + (float(fabric_cost_four)* float(yard_need_four))
        else:
            print("You did not enter a number of fabrics that can be processed by the calculator.")

trimnumber = input("How many trims does your garment need? Enter up to four")

    def trim_cost(trimnumber)
        if trimnumber == "1":
            trim_need_one= input("Number of Trim 1 needed: ")
            trim_cost_one= input("Cost of Trim 1: ")
            trimcost= float(trim_cost_one )* float(trim_need_one)

        elif fabricnumber == "2":
            trim_need_one = input("Numberof Trim 1 needed: ")
            trim_cost_one= input("Cost of Trim 1: ")
            trim_need_two = input("Number of Trim 2 needed: ")
            trim_cost_two= input("Cost of Trim 2: ")
            trim_cost= (float(trim_cost_one )* float(trim_need_one)) + (float(trim_cost_two)* float(trim_need_two))

        elif fabricnumber == "3":
            trim_need_one = input("Number of Trim 1 needed: ")
            trim_cost_one= input("Cost of Trim 1: ")
            trim_need_two = input("Number of Trim 2 needed: ")
            trim_cost_two= input("Cost of Trim 2: ")
            trim_need_three = input("Number of Trim 3 needed: ")
            trim_cost_three= input("Cost of Trim 3: ")
            trim_cost= (float(ftrim_cost_one )* float(trim_need_one)) + (float(trim_cost_two)* float(trim_need_two)) + (float(trim_cost_three)* float(trim_need_three))

        elif fabricnumber == "4":
            trim_need_one = input("Number of Trim 1 needed: ")
            trim_cost_one= input("Cost of Trim 1: ")
            trim_need_two = input("Number of Trim 2 needed: ")
            trim_cost_two= input("Cost of Trim 2: ")
            trim_need_three = input("Number of Trim 3 needed: ")
            trim_cost_three= input("Cost of Trim 3: ")
            trim_need_four = input("Number of Trim 4 needed: ")
            trim_cost_four= input("Cost of Trim 4: ")
            trim_cost= (float(trim_cost_one )* float(trim_need_one)) + (float(trim_cost_two)* float(trim_need_two)) + (float(trim_cost_three)* float(trim_need_three)) + (float(trim_cost_four)* float(trim_need_four))
        else:
            print("You did not enter a number of fabrics that can be processed by the calculator.")

tagnumber = input("Do you have a hang tag and/or garment tag?")

    def tag_cost(tagnumber)
        if tagnumber == "Yes" or "yes"
            tagcostone = input("Enter cost of hang tag:")
            tagcosttwo = input("Enter cost of garment tag:")
            tagcost = tagcostone + tagcosttwo
        else:
            continue

markuprate = input("Enter your markup rate:")

    def materials_cost():
        materialscost = tagcost + trim_cost + fabric_cost + 

    def wholesale_price():
        wholesale_price = materialscost * markuprate

    def 
        

    




