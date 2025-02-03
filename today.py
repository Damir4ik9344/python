def check_password(password):
    correct_password = "Academy24"
    if password == correct_password:
        return True
    return False


def brute_force(password_list):
 for password in password_list:
    print("Checking password:{password}")
    if check_password(password):
        print("ACCESS GRANTED!Password is {password}")
         return password
print("ACCESS DANTED !Password is {password}")
return None


passwords = [
hX7#uF9&bLp
T9jH*2q$VwT1
mNr8$zP1tQx
4kTpR9!wXsE
cV6jK0@dZlM
gWf$7Hp3mYq
vJ7#e8zZxFg
WnU2$R1hFbZ
p3GvQy$L9Js
F!sR0t8VbWz]

password = [password.strip() for password in passwords]
brute_force(passwords)




    
