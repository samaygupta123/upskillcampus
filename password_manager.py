while True:
    print("Press 1 to add New password")
    print("Press 2 to view existing passwords")
    print("Press 3 to exit")
    
    userChoice = input("Enter your choice: ")
    
    if userChoice =="1":
        website=input("Enter website name/url: ")
        userName= input("Enter username: ")
        password=input("Enter password: ")
        #print(website,userName,password)
        
        with open("passwords.txt","a") as file: 
            file.write(f"{website} | {userName} | {password}\n")
            
        print("Password added successfully!")
         
    elif userChoice=="2":
        with open ('passwords.txt','r')as file:
            print(file.read())
    
    elif userChoice=="3":
        print("Thank You!")
        break
    
    else:
        print("Invalid choice! Please try again.")