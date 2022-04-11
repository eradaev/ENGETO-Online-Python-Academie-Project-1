# Text Analyzer
from pprint import pprint
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

texts_numbers = ("1", "2", "3")
oddelovac = "-"

# Registered users' data
registered_users = {"bob": "123",
                    "ann": "pass123",
                    "mike": "password123",
                    "liz": "pass123"
}

# Ask user for login and password
username = input("Username: ")
password = input("Password: ")
print(oddelovac * 40)

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if registered_users.get(username) == password:

    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print(f"""Welcome to the app, {username}! \nWe have 3 texts to be analyzed.""")
    print(oddelovac * 40)

# pokud není registrovaný, upozorni jej a ukonči program
else:
    print(f"""User not found! Terminating the program! """)
    print(oddelovac * 40)
    quit()
choice = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac * 40)
if choice not in texts_numbers:
    print(f'Wrong choice!')
    quit()
else:
    selected_text = TEXTS[int(choice) - 1]
#   print(selected_text)

# Calculate the number of words in the selected text
text_list = selected_text.split()
text_list_cleaned = []
for word in text_list:
    text_list_cleaned.append(word.strip(".,:!\"\'"))
print(f"""There are {len(text_list_cleaned)} words in the selected text.""")

# Calculate the number of titlecase words in the selected text
text_list_titlecase = []
for index in range(0, len(text_list_cleaned)):
    if text_list_cleaned[index].istitle():
        text_list_titlecase.append(text_list_cleaned[index])
print(f"""There are {len(text_list_titlecase)} titlecase words.""")

# Calculate the number of uppercase words in the selected text
text_list_uppercase = []
for index in range(0, len(text_list_cleaned)):
    if text_list_cleaned[index].isupper():
        text_list_uppercase.append(text_list_cleaned[index])
print(f"""There are {len(text_list_uppercase)} uppercase words.""")
# print(text_list_uppercase)

# Calculate the number of lowercase words in the selected text
text_list_lowercase = []
for index in range(0, len(text_list_cleaned)):
    if text_list_cleaned[index].islower():
        text_list_lowercase.append(text_list_cleaned[index])
print(f"""There are {len(text_list_lowercase)} lowercase words.""")
# print(text_list_lowercase)

# Calculate the number of numeric strings
text_list_numeric = []
for index in range(0, len(text_list_cleaned)):
    if text_list_cleaned[index].isnumeric():
        text_list_numeric.append(text_list_cleaned[index])
print(f"""There are {len(text_list_numeric)} numeric strings.""")

# Calculate the sum of all the numbers
text_list_numeric_int = [int(i) for i in text_list_numeric]
sum_numbers = sum(text_list_numeric_int)
print(f"""The sum of all the numbers is {sum_numbers}.""")
print(oddelovac * 40)

# Word length frequency bar chart

print(f"LEN|     OCCURENCES     |NR.")
print(oddelovac * 40)

graph = "*"
space = " "
length_frequency = {}
for word in text_list_cleaned:
    if len(word) not in length_frequency:
        length_frequency[len(word)] = 1
    else:
        length_frequency[len(word)] = length_frequency[len(word)] + 1
length_frequency_sorted = sorted(list(length_frequency.items()), reverse=False)

for i in length_frequency_sorted:
    print(f"{i[0]:>3}|{graph * i[1]}{(20 - i[1]) * space}|{i[1]}")
print(oddelovac * 40)