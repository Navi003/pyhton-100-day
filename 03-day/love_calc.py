name1 = input("Enter first  name") 
name2 = input("Enter second name")

T = name1.lower().count('t') + name2.lower().count('t')
R = name1.lower().count('r') + name2.lower().count('r')
U = name1.lower().count('u') + name2.lower().count('u')
E = name1.lower().count('e') + name2.lower().count('e')

L = name1.lower().count('l') + name2.lower().count('l')
O = name1.lower().count('o') + name2.lower().count('o')
V = name1.lower().count('v') + name2.lower().count('v')
E = name1.lower().count('e') + name2.lower().count('e')


value_true = T+R+U+E
value_love = L+O+V+E


sum = int(f"{value_true}{value_love}")

if sum < 10 or sum > 90:
    print(f"Your score is {sum}, you go together like coke and mentos.")
elif sum >= 40 and sum <= 50:
    print(f"Your score is {sum}, you are alright together.")
else:
    print(f"Your score is {sum}")