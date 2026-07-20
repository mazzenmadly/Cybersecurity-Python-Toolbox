import random

def password_generator():
    length= int(input("please enter the length of the password :"))
    charset = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if length< 8 :
        print("the password is too short ")
    else :    
        password = ''.join(random.choices(charset, k=length))    
        print("your password is" ,password)

password_generator()