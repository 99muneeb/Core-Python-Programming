letter = '''Dear <|NAME|>,
Greetings from pny coding house. I am happy to tell you about your selection
You are selected!
Have a great day <|NAME|>!
Regard: <|Hr_Regard|>
Date: <|DATE|>
'''

name = input("Enter Your Name\n")
Regard = input("Enter Hr pny trainings Regard\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|Hr_Regard|>", Regard)
letter = letter.replace("<|DATE|>", date)
print(letter)
