from cgitb import html
import random
import string
import names

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


domains = [ "hotmail.com", "gmail.com", "yahoo.com"]


def get_one_random_domain(domains):
    return domains[random.randint( 0, len(domains)-1)]
    
def generate_details(lenght):
    for i in range(lenght):
        print("\nName : ",names.get_full_name()) 
        upper_case=1
        name_upper_chars = string.ascii_uppercase
        upper_name = ''.join(random.choice(name_upper_chars) for y in range(upper_case))
        name_chars = string.ascii_lowercase
        name = ''.join(random.choice(name_chars) for x in range(1,14))    
        print("Username : ",upper_name + name )
        one_domain = str(get_one_random_domain(domains))    
        print("Email : ",names.get_first_name()+names.get_last_name()+"@"+one_domain)  
        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all,18))
        print("Password : ",password)
        
       
length=int(input("Enter the lenght : "))     
generate_details(length)
