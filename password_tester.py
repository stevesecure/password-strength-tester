#!/usr/bin/env python3

def check_length(p): return "Pass" if len(p) >= 8 else "Fail"
def check_uppercase(p): return "Pass" if any(c.isupper() for c in p) else "Fail"
def check_lowercase(p): return "Pass" if any(c.islower() for c in p) else "Fail"
def check_digit(p): return "Pass" if any(c.isdigit() for c in p) else "Fail"
def check_special(p): 
    return "Pass" if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in p) else "Fail"

def main():
    print("\033[96m=== Password Strength Tester ===\033[0m\n")
    password = input("Enter a password to test: ").strip()
    
    results = [
        ("Length ≥8     ", check_length(password)),
        ("Uppercase      ", check_uppercase(password)),
        ("Lowercase      ", check_lowercase(password)),
        ("Digit          ", check_digit(password)),
        ("Special char   ", check_special(password)),
    ]
    
    score = sum(1 for _, status in results if status == "Pass")
    
    print(f"\nYou entered: {password}\n")
    for test, status in results:
        color = "\033[92m" if status == "Pass" else "\033[91m"
        print(f"{color}{test}: {status}\033[0m")
    
    print(f"\nScore: {score}/5", end="")
    if score == 5:
        print("  \033[92m→ STRONG\033[0m")
    elif score >= 3:
        print("  \033[93m→ MEDIUM\033[0m")
    else:
        print("  \033[91m→ WEAK\033[0m")

if __name__ == "__main__":
    main()
