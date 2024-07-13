import random as rand
import string as str

def generate_password(length,complexity):
    password = ""
    characters = str.ascii_letters
    numbers = False
    special_characters = False

    if complexity == 2:
        characters += str.digits
        numbers = True
    elif complexity == 3:
        characters += str.digits + str.punctuation
        numbers = True
        special_characters = True

    criteria = False
    has_letter = False
    has_number = False
    has_specialCharacters = False

    while not criteria or len(password) < length:
        character = rand.choice(characters)

        if character in str.ascii_letters:
            has_letter = True
        if character in str.digits:
            has_number = True
        if character in str.punctuation:
            has_specialCharacters = True

        criteria = has_letter

        if numbers:
            criteria = has_letter and has_number
        if special_characters:
            criteria = criteria and has_specialCharacters

        password += character

        if len(password) == length and not criteria:
            password = ""
            has_letter = False
            has_number = False
            has_specialCharacters = False

    return password

print("------PASSWORD GENERATOR------\n")

x = True
while x:
    length = int(input("Enter the length of the password (Minimum length 3): "))
    if length >= 3:
        x = False

print("Choose one of the following complexity levels: ")
print("1.Normal (Include only letters)\n"
      "2.Medium (Include letters and numbers)\n"
      "3.Strong (Include letters,numbers and special characters)\n")

y = True
while y:
    choice = int(input("Enter your choice (corresponding number of your choice): "))
    if choice>=1 and choice<=3:
        y = False

result = generate_password(length,choice)
print("The generated password is",result)
