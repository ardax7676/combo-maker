print("Welcome To Combo Maker")

    
users = input("User List's Direction: ")
passwords = input("Password list's Direction: ")
     
combo = []

try:
    user = open(users,"r")
    password = open(passwords,"r")
    


    for a,b in zip(user.readlines(),password.readlines()):
        
        if a.endswith("\n") or b.endswith("\n"):
            a = a[:-1]
            
        combo += [a,":",b]
        
    with open("result.txt","w") as f:
        f.writelines(combo)
        
        user.close()
        password.close()
        
except FileNotFoundError or NameError:
    print("File Not Found!")
