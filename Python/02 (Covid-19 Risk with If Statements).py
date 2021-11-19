age = input(
    "Are you a cigarette addict older than 75 years old? eg.(Yes/No) ").title().strip()
chronic = input(
    "Do you have a severe chronic disease? eg.(Yes/No) ").title().strip()
immine = input("Is your immune system too weak? eg.(Yes/No) ").title().strip()
if age == "Yes":
    age = True
else:
    age = False
if chronic == "Yes":
    chronic = True
else:
    chronic = False
if immine == "Yes":
    immine = True
else:
    immine = False
if age and chronic and immine == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
