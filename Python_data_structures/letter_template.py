letter=('''Dear  <|Name|>
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day Muneeb!
Thanks and regards,
Bill
Date: <|date|>''')
name=input("Enter you name: ")
date=input("Enter today date: ")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)


