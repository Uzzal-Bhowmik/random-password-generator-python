import random

# THIS FUNCTION IS TO SHUFFLE THE PASSWORD 
def to_shuffle(passw):
    passw = list(passw)
    random.shuffle(passw)
    passw = "".join(passw)
    return passw

# THIS IS THE MAIN FUNCTION TO GENERATE THE RANDOM PASSWORDS
def rand_pass():
    for_upal = random.randint(65,90)
    for_upal1 = random.randint(65,90)

    for_lowal = random.randint(97,122)
    for_lowal1 = random.randint(97,122)

    for_symbols = random.randint(33,43)
    for_symbols1 = random.randint(33,43)

    for_digit = random.randint(0,9)
    for_digit1 = random.randint(0,9)

    password = (chr(for_upal) + chr(for_lowal) + chr(for_upal1) + chr(for_symbols) + chr(for_lowal1) + str(for_digit)
                + str(for_digit1) + chr(for_symbols1))

    password = to_shuffle(password)
    return password

# THIS FUNCTION WILL PRODUCE A PASSWORD THAT IS RELATED TO THE USERS
def r_to_y_pass():
    yname = input(("What's Your Name? -> ").strip().title())
    yb_year = input("What's Your Birth-Year?(yyyy) -> ")
    yfav_num = int(input("What's Your Favourite Number?(0-9) ->"))
    for_symbols2 = random.randint(33,43)
    for_symbols3 = random.randint(33,43)
    
    password = yname[0] + yb_year[0] + yb_year[1] +chr(for_symbols2) + yb_year[2] +yb_year[3]  + str(yfav_num) + chr(for_symbols3) + yname[len(yname)-1] 
#     password = to_shuffle(password)
    return password

# WELCOME MESSEGE
welcome_msg = " Welcome To Random PassWord-Generator "
print(welcome_msg.center(52,"-"))

# HOMEPAGE MENU
hpage_msg = int(input("What type of password you want?\n1> Computer Generated Random Password\n2> Related To You\n->"))

if hpage_msg == 1:

    num_of_pass = int(input("\nHow many passwords you want?:- "))
    n = 0

    for i in range(num_of_pass):
        random_pass = rand_pass()
        n += 1
        print(f"Pass-{n}:- {random_pass}")
        
elif hpage_msg == 2:
    rela_pass = r_to_y_pass()
    print(f"Password: {rela_pass}")
    

    
# ENDING MESSEGE
end_msg = " Happy Password Choosing !!! "
print("\n" + end_msg.center(40,"-"))