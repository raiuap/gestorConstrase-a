from encrypt import AES256
from save import Saver
import os

masterPasswordCheck= b'xkR2MEaUE81KQPn8SRhUBqbXmm/CO7wpNWd5iobEbnI='



saver= Saver("password.txt")
password= saver.read()
loogedIn= False

while True:
    if not loogedIn:
        print("Master Password: ", end="")
        masterPassword= input()

        encrypter= AES256(masterPassword)

        if encrypter.encrypt("Bonjour1")!= masterPasswordCheck:
            print("Password is incorrect")
            input()
            continue
        else:
            loogedIn= True
    
    os.system("clear")

    print("1. Find Password")
    print("2. Add Password")
    print("3. Delete Password") 

    print("\nChoice:", end="") 
    choice= int(input())

    if choice < 1 or choice > 3:
        print("Choice needs to be a number from 1-3")
        input()
        continue

    print("Application Nmae: ", end="")
    app=input()

    if choice == 1:
        for entry in password:
            if app in encrypter.decrypt(entry[0]):
                print("\n------------------------------------------")
                print("Application: ", encrypter.decrypt(entry[0]))
                print("Password: ", encrypter.decrypt(entry[1]))
        input()

    elif choice == 2:
        print("Password: ", end="")
        app_password= input()
        password.append([encrypter.encrypt(app).decode(), encrypter.encrypt(app_password).decode()])
        saver.save(password)

    elif choice == 3:
        for entry in password:
            if app in encrypter.decrypt(entry[0]):
                print("Are you sure you want to delete '{app}'? (y/n): ", end="")
                confirm= input()

                if confirm == "y":
                    del password[password.index(entry)]
                    saver.save(password)


                break




