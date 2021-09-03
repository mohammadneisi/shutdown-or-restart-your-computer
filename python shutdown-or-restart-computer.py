
import os
print("1 , immediate shutdown computer.")
print("2 , timed shutdown of the computer. ")
print("3 , immediate restart computer.")
print("4 , timed restart of the computer. ")
print("5 , exit")
print(end="enter your choice : ")

choice = int(input())

if choice ==1 :
    os.system("shutdown /s /t 0")

elif choice == 2:
    print(end= "enter your time for shutdown : ")
    sec = int(input())
    str_one = "shutdown /s /t"
    str_two = str(sec)
    str = str_one + str_two
    os.system(str)

elif choice == 3:
    os.system("shutdown /r /t 0")

elif choice == 4 :
    print(end= "enter your time for restart : ")
    sec = int(input())
    str_one = "shutdown /r /t"
    str_two = str(sec)
    str = str_one + str_two
    os.system(str)

elif choice ==5:
    exit()

else :
    print("your choice is wrong!!")

















