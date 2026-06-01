def alphabatical_cesar_shift(string, shifting_parameter):
    while True:
        string = input("Please enter your string: ")
        shifting_parameter = int(input("Great! Now please enter the shifting parameter: "))
        print()
        result = []
        for char in string:
            if 'A' <= char <= 'Z':
                shifted = ord('A') + ((ord(char) - ord('A') + shifting_parameter) % 26)
                result.append(chr(shifted))
            elif 'a' <= char <= 'z':
                shifted = ord('a') + ((ord(char) - ord('a') + shifting_parameter) % 26)
                result.append(chr(shifted))
            else:
                result.append(char)
        print("The ciphered/deciphred string is: '" + "".join(result) + "'")
        print()
        user_end = input("Would you want to do another cipher/decipher? (enter y for yes and n for no) ")
        print()
        if user_end.lower() == "y":
            continue
        elif user_end.lower() == "n":
            break

def ascii_cesar_shift(input_string,shifting_parameter):
    while True:
        input_string = input("Please enter your string: ")
        shifting_parameter = int(input("Great! Now please enter the shifting parameter: "))
        result_list = []
        for char in input_string:
            code = ord(char)
            if 33 <= code <= 126:
                shifted = 33 + ((code - 33 + shifting_parameter) % 94)
                result_list.append(chr(shifted))
            else:
                result_list.append(char)
        print("".join(result_list))
        user_end = input("Would you want to do another cipher/decipher? (enter y for yes and n for no) ")
        print()
        if user_end.lower() == "y":
            continue
        elif user_end.lower() == "n":
            break

def base64_encode_decode(input_string):
    import base64
    while(True):
        input_string = input("Please enter your string: ")
        encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        print("Encoded string: " + encoded_string)
        try:
            decoded_bytes = base64.b64decode(input_string.encode('utf-8'))
            decoded_string = decoded_bytes.decode('utf-8')
            print("Decoded string: " + decoded_string, end="\n")
        except Exception as e:
            print("Error occurred while decoding:", e)
        user_end = input("Would you want to do another encode/decode? (enter y for yes and n for no) ")
        print() 
        if user_end.lower() == "y":
            continue
        elif user_end == "n":
            break

def sha256_MD5_hashing(input_string):
    import hashlib
    while(True):
        input_string = input("Please enter your string: ")
        sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()
        print("SHA-256 Hash: " + sha256_hash)
        print("MD5 Hash: " + md5_hash)
        user_end = input("Would you want to do another hashing? (enter y for yes and n for no) ")
        print() 
        if user_end.lower() == "y":
            continue
        elif user_end.lower() == "n":
            break

def main():
    import time
    first_time = True
    while(True):
        if first_time:
            print("Welcome to this lovely program!")
            first_time = False
        print("What would you like to do?")
        print("1. Alphabatical Caesar Shift")
        print("2. ASCII Caesar Shift")
        print("3. Base64 Encode/Decode")
        print("4. Sha256 and MD5 Hashing")
        print("0. Exit")
        user_choice = input("Please enter the number of your choice: ")
        print()
        if user_choice == "1":
            alphabatical_cesar_shift("","")
        elif user_choice == "2":
            ascii_cesar_shift("","")
        elif user_choice == "3":
            base64_encode_decode("")
        elif user_choice == "4":
            sha256_MD5_hashing("")
        elif user_choice == "0":
            print("Come back anytime!")
            for i in range(3,0, -1):
                print(f"\rExiting in {i}", end = "")
                time.sleep(1)
            print("\rExiting now!   ")
            time.sleep(0.5)
            break
        else:
            print("Invalid input! Please try again.")
            print()

if __name__ == "__main__": 
    main()