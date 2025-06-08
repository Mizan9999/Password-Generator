import secrets
import string

def generate_strong_password(length):
    """Generate a cryptographically secure password with guaranteed character diversity"""
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Ensure at least one character from each set
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]
    
    # Fill remaining characters
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))
    
    # Shuffle and return as string
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    print("🔐 STRONG PASSWORD GENERATOR")
    print("----------------------------")
    
    while True:
        try:
            # Get user input with clear instructions
            length = int(input("\nEnter password length (minimum 8): "))
            
            if length < 8:
                print("❌ Password must be at least 8 characters! Try again.")
                continue
                
            # Generate and display password
            password = generate_strong_password(length)
            print(f"\n✅ Your {length}-character secure password:")
            print(f"   {password}")
            print("\n" + "="*50)
            
            # Continue prompt
            if input("\nGenerate another? (y/n): ").lower() != 'y':
                print("\n🔒 Stay secure! Goodbye.")
                break
                
        except ValueError:
            print("⚠️ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()