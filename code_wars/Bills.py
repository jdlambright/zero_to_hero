bills_on_5 = {
    "mortgage": 784.03,
    "pcu": 250,#$12000
    "travel": 85, #$7883.30
    "discover": 120,#$6000
    "destination": 160,#$1200
    "verizon": 85,
}

cc_debt = [12000,7883.3,6000,1200,7936,5541]

print(f"You have a total of ${sum(cc_debt)} in credit card debt\n")

fifth = bills_on_5.values()
fifth_totals = sum(fifth)
print(f"Your total bills that come out around the 5th is ${fifth_totals}")


cc_bills_on_5 = {
    "destination": 160,
    "verizon": 85,
}

cc_fifth = cc_bills_on_5.values()
cc_fifth_totals = sum(cc_fifth)
print(f"${cc_fifth_totals} of those bills will be paid by credit card\n")

bills_on_20 = {
    "pilot": 229.78,
    "josh_life": 69.10,
    "citi": 121.00, #$7936.06
    "car_ins": 122.96,
    "student_loan": 104.68,
    "kelly_cash": 160, #$5541.32
    "kelly_life": 25.02,
    "electric": 153.24,
    "internet": 74.73,
    "evergreen": 33,
    "destination": 160,
}
twentieth = bills_on_20.values()
twentieth_totals = sum(twentieth)
print(f"Your total bills that will come out around the 20th is ${twentieth_totals}")

cc_bills_on_20={
    "electric": 153.24,
    "internet": 74.73,
    "evergreen": 33,
    "destination": 160,
}

cc_twentieth = cc_bills_on_20.values()
cc_twentieth_totals = sum(cc_twentieth)
print(f"${cc_twentieth_totals} of those bills will be paid by credit card\n")

print(f"Your total monthly bills are ${fifth_totals + twentieth_totals}")
print("Your montly income is $3036.94")

