#PRODIGY INFOTECH
#TASK-01 : Caesar Cipher - Encrypt & Decrypt Text


def caesar_cipher(text,shift,mode):
    """
    Encrypts or Decrypts text using the Caesar Cipher algorithm
    mode: 'encrypt' or 'decrypt'
    """
    result=""
    if mode =='decrypt':
        shift = -shift #Reverse the shift for decryption

        for char in text:
            if char.isalpha():
                #determine uppercase or lowercase
                base = ord('A') if char.isupper() else ord('a')
                #apply shift with wrap-around using module 26
                shifted = (ord(char) - base + shift)%26
                result += char(base + shifted)
            else:
                #Non alphabetical characters(spaces,number,symbols)unchanged
                result += char

        return result


def get_shift_value():
     """prompts user for a valid shift value(1-25)"""
     while True:
         try:
             shift = int(input("Enter shift value(1-25): "))
             if 1<= shift <=25:
                 return shift
             else:
                print(" ! Shift must be between 1 and 25 . Try Again")
         except ValueError:
             print(" ! Invalid input . please enter a number .")


def main():
    print("=" * 50)
    print(" CAESAR CIPHER - Prodigy InfoTech Task-01")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print(" 1. Encrypt a message")
        print(" 2. Decrypt a message")
        print(" 3. Exit")

        choice = input("\nEnter  your choice (1/2/3): ").strip()

        if choice == '1':
            message = input("Enter a message to Encrypt :")
            shift = get_shift_value()
            encrypted = caesar_cipher(message,shift,'encrypt')
            print(f"\n Original :{message}")
            print(f" shift  : {shift}")
            print(f" Encrypted : {encrypted}")

        elif choice == '2':
            message = input("Enter message to Decrypt :")
            shif = get_shift_value()
            decrypted = caesar_cipher(message,shift,'decrypt')
            print(f"\n Encrypted : {message}")
            print(f" shift : {shift}")
            print(f" Decrypted : {decrypted}")

        elif choice == '3':
            print("\n Exiting Caesar Cipher tool . ")
            break
        else:
            print("! invalid choice . please enter 1,2,3 . ")


if __name__ == "__main__":
    main()
    






























