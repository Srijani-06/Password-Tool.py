# Password-Tool.py
Python password tool with two features: generates strong random password and checks any password's strength (weak/medium/strong)
## Features

### 1. Password Generator
- Generates a random password of a given length
- Guarantees at least one lowercase letter, one uppercase letter, one digit, and one symbol
- Shuffles characters so the guaranteed ones aren't in predictable positions

### 2. Password Strength Checker
- Takes any password as input
- Checks length, character variety (lowercase, uppercase, digits, symbols) using regex
- Returns a strength rating: Weak / Medium / Strong
- Gives specific suggestions for what's missing (e.g. "Add uppercase", "Make it at least 8 characters")

## Concepts Practiced
- String operations (concatenation, slicing)
- The `random` module (`random.choice`, `random.shuffle`)
- The `re` module (regex pattern matching)
- Functions returning multiple types of feedback

## How to Run
python password-tool.py

## Sample Output
Enter Your Password: hjy763F#$
Strength: Medium
Suggestions:
- Add uppercase
