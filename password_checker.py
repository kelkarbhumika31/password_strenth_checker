password = input("Enteer your password: ")

if len(password) >= 8:
    print("✔ Good length")
else:
    print("✘ Password should be at least 8 characters")

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_symbol = True

if not has_upper:
    print("✘ Add at least one uppercase letter")

if not has_lower:
    print("✘ Add at least one lowercase letter")

if not has_digit:
    print("✘ Add at least one number")

if not has_symbol:
    print("✘ Add at least one special character")

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

if score <= 2:
    print("Password Strength: WEAK")
elif score == 3 or score == 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")