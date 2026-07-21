import random
import string
import re 

password = input("Enter Your Password: ")
pass_len = 10
has_digit = re.search(r"[0-9]",password)
print(has_digit)

values = (string.ascii_letters + string.digits + string.punctuation)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

gurranteed_lower = random.choice(lower)
gurranteed_upper = random.choice(upper)
gurranteed_digits = random.choice(digits)
gurranteed_symbols = random.choice(symbols)

remaining_char = 10 - 4
gurranteed_char = [gurranteed_lower , gurranteed_upper , gurranteed_digits, gurranteed_symbols]
extra_char =[random.choice(values) for i in range(remaining_char)]
all_char = gurranteed_char + extra_char

has_lower = re.search(r"[a-z]" , password)
has_upper = re.search(r"[A-Z]", password)
has_symbols = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

password_new = (has_lower,has_upper,has_symbols,has_digit)

length_ok = len(password) >= 8

score = 0 
if length_ok :
    score += 1 
if has_lower:
    score += 1 
if has_upper:
    score += 1  
if has_symbols:
    score += 1 
if has_digit:
    score += 1 

if score <= 2 :
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

suggestions = []
if not length_ok:
    suggestions.append("Make It Atleast 8 Character long")
if not has_lower:
    suggestions.append("Add Lowercase")
if not has_upper:
    suggestions.append("Add Uppercase")
if not has_symbols :
    suggestions.append("Add Symbols")
if not has_digit :
    suggestions.append("Add Digits")

print("Strength : " , strength)
if suggestions:
    print("Suggestions : ")
    for tip in suggestions:
        print("-", tip)
else:
    print("Great Password")

random.shuffle(all_char)
final_pass = "".join(all_char)

print( "YOUR Suggestion PASSWORD IS: ",final_pass)





















