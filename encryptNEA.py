# author information
author = "Marcus Sorensen"
date = "09/12/20, during math class"
reason = "To help yr13 with NEA"

# dependencies -- default python libraries (no external libraries used)
import time
import string

# <<information gathering functions>>
    # cipher info
def edinfo():
    info = []

    ciphertype = input("What type of cipher would you like to use? rot [r] or vernam [v]\t")
    info.append(ciphertype)
    eord = input("Would you like to encode or decode a message? encode [e] or decode [d]\t")
    info.append(eord)

    return info

    # cipher data
def getdata(type, eord):
    if type.lower() == "r":

        if eord.lower() == "e":
            plaintext = input("What message would you like to encode?\t")
            rotnum = input("What rotational number would you like to use to encode your message?\t")
            return [plaintext,rotnum]

        elif eord.lower() == "d":
            ciphertext = input("What is the message you'd like decoded?\t")
            rotnum = input("What rotational number would you like to use to decode the message?\t")
            return [ciphertext,rotnum]

        else:
            print("Erroneous data inputted, restarting program...")
            time.sleep(3)
            main()

    elif type.lower() == "v":

        if eord.lower() == "e":
            plaintext = input("What message would you like to encode?\t")
            otp = input("What one-time pad would you like to use to encode your message?\t")
            return [plaintext, otp]

        elif eord.lower() == "d":
            ciphertext = input("What is the message you'd like decoded?\t")
            otp = input("What one-time pad would you like used to decode your message?\t")
            return [ciphertext, otp]

        else:
            print("Erroneous data inputted, restarting program...")
            time.sleep(3)
            main()

    else:
        print("Erroneous data inputted, restarting program...")
        time.sleep(3)
        main()

# <<encoding / decoding functions>>
    # <<rot cipher / caesarian cipher>>
def rot(ed, data):
    try:
        data[1] = int(data[1])
    except TypeError:
        print("invalid rot number")

    if ed == "e":
        encryptedmessage = ''
        message = data[0]
        rot = data[1]

        for i in range(len(message)):
           char = message[i]

           if char == ' ':
               encryptedmessage += ' '
           elif (char.isupper()):
               encryptedmessage += chr((ord(char) + rot-65) % 26 + 65)
           elif (char.islower()):
               encryptedmessage += chr((ord(char) + rot-97) % 26 + 97)
           else:
               print("Erroneous data inputted, restarting program...")
               time.sleep(3)
               main()

        print(f"Your Encrypted Message is: [{encryptedmessage}]")
        time.sleep(3)
        carryon()

    elif ed == "d":
        decryptedmessage = ''
        message = data[0]
        rot = data[1]
        rot = 26 - rot

        for i in range(len(message)):
           char = message[i]

           if char == ' ':
               decryptedmessage += ' '
           elif (char.isupper()):
               decryptedmessage += chr((ord(char) + rot-65) % 26 + 65)
           elif (char.islower()):
               decryptedmessage += chr((ord(char) + rot-97) % 26 + 97)
           else:
               print("Erroneous data inputted, restarting program...")
               time.sleep(3)
               main()
        print(f"Your decrypted message is: [{decryptedmessage}]")
        time.sleep(3)
        carryon()

    else:
        print("error :/")

        print(f"Your Decrypted Message is: [{decryptedmessage}]")
        time.sleep(3)
        carryon()
    
    # <<vernam cipher>>
    # coop with Igor Michalec
def vernam(ed, data):
    if ed == "e":
        plaintext = data[0]
        key = data[1]
        code = ""
        if len(key) >= len(plaintext):
            for i in range(len(key)):
                try:
                    kb = ord(plaintext[i])^ord(key[i])
                except:
                    kb = ord(key[i])
                code += str(kb)+" "
            print(f"Your encrypted message is: [{code}]")
            time.sleep(3)
            carryon()

        else:
            print("Invalid key entered, restarting program...")
            time.sleep(3)
            main()

    elif ed == "d":
        ciphertext =list(map(int,data[0].split()))
        key = data[1]
        code = ""
        if len(key) == len(ciphertext):
            for i in range(len(key)):
                kb = ciphertext[i]^ord(key[i])
                code += chr(kb)
            print(f"Your decrypted message is: [{code}]")
            time.sleep(3)
            carryon()

        else:
            print("Invalid key entered, restarting program...")
            time.sleep(3)
            carryon()

    else:
        print("error :/")

# <<carryon procedure>>
def carryon():
    x = input("Would you like to carry on encrypting or decrypting? [Y] or [N]:\t")
    x = x.lower()

    if x == 'y':
        main()
    elif x == 'n':
        print("Ok.")
        time.sleep(2)
        exit()
    else:
        print('Error. Please enter either [Y] or [N].\nYou will be redirected in 2 seconds.')
        carryon()

# <<main>>
def main():
    print("this is the vernam/rot cipher en/de coder, enjoy")
    info = edinfo()
    data = getdata(info[0], info[1])
    if info[0].lower() == "r":
        if info[1].lower() == "e":
            rot("e", data)
        elif info[1].lower() == "d":
            rot("d", data)
        else:
            print("Erroneous data inputted, restarting program...")
            time.sleep(2)
            main()
    elif info[0].lower() == "v":
        if info[1].lower() == "e":
            vernam("e", data)
        elif info[1].lower() == "d":
            vernam("d", data)
        else:
            print("Erroneous data inputted, restarting program...")
            time.sleep(2)
            main()

#  > run
main()