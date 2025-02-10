def check_password(password):
    correct_password = "gWf$7Hp3mYq"
    if password == correct_password:
        return True
    return False

def brute_force(password_list):
    for password in password_list:
        print(f"Checking password:{password}")
        if check_password(password):
            print(f"ACCESS GRANTED! {password}")
            return password
    print("ACCESS DANTED!")
    return None


passwords = ["hX7#uF9&bLp", 
"T9jH*2q$VwT1",
"kTpR9!wXsE",
"cV6jK0@dZlM",
"gWf$7Hp3mYq",
"vJ7#e8zZxFg",
"WnU2$R1hFbZ",
"p3GvQy$L9Js",
"F!sR0t8VbWz"]

brute_force(passwords)




    
