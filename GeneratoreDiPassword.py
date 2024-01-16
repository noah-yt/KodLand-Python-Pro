import termcolor
import random
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passw = ""
for i in range(int(input("numero caratteri: "))):
    passw += (char[random.randint(0,71)])
    print(termcolor.colored(passw,"green"))


if input(termcolor.colored("salvare a file? [y/n] ", "red")) == "y":
    with open("password.txt", "w") as f:
        f.write(passw)
