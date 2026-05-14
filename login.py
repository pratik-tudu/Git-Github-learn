passw="123"
input_pass="123"
def passcheck(str_pass):
    if(str_pass == passw):
        print("login succesfull")
    else:
        print("Incorrect Pass")
passcheck(input_pass)

print("Login resolved ..")