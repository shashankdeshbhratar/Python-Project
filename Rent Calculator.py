# Rent Calculator


rent = int(input("Total rent/flat: "))
food = int(input("Tota food cost: "))
electricity_spend = int(input("Total electricity spend: "))
charge_per_unit = int(input("Enter charge_per_unit: "))
persons = int(input("Enter number of persons: "))

total_electricity = electricity_spend * charge_per_unit

total_bill = ( rent + food + total_electricity ) // (persons)

print("Total bill of Rent is: ",total_bill)


