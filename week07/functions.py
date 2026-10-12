#exercise 1
def calculate_tax(price,rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"tax for $100 at 7%: ${tax1:.2f}")
print(f"tax for $250 at 8%: ${tax2:.2f}")
print(f"tax for 350 at 5%: ${calculate_tax(350, 0.05):.2f}")




#exercise 2
def apply_discount(price,tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price,tier):.2f}")

#exercise 3
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold')= {final_price(200, 0.07, "gold"):.2f}")

#exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"price: ${price} | tier:{tier} | final: ${total:.2f}")


#exercise 6

x = 100

def double_it():
    x=999
    return x * 2

print(x)  #100
print(double_it())  #1998
print(x)  #100, the global x is used not x in the function.
#scope is essentially where the variable can be used, if you define a variable outside a function that is the value everythingwill use, it is global.
#However if you if you efine a variable in a function without using return it will never stor ethe value that is why 999 didnt appear in the first or second print statements.


#self assessment
#1. The first bug I noticed was the missing colon in the for statement, I figured this out by doing using a print statement. I think this means I can recognize basic structural issues from a error statement prettyeasily.
#2 apply_discount takes the inputs tier and price takes a particular tier gold, silver or bronze and applies a corresponding discount. I think someone could use the function without explanation it is pretty self explanatory.
#3. #AI DISCLOSURE STATEMENT
#Model: claude Sonnet 5.5
#Prompt: I pasted the error traceback from my code straight into Claude.
#Adaptation: I read the explanation of what was wrong and thought of how to fix it. Claude offered a solution but I used a simpler method. I just needed to make the sign in "i <= len(sales)" a < in the while statement in broken_sales.py
#I think the AI helped me understand better because I just wanted it to identify what was breaking, I dont think it shortcutted my learning because I had talked to a rubber duck before hand and I still couldn't identify the bug.

