import os
import time
import fade
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def ip_info():
    RED = "\033[91m"
    RESET = "\033[0m"
    ipl = input("[+] enter ip: ")
    url = requests.get(f"https://ipinfo.io/{ipl}/json").json()
    not_f = "not found"
    not_fo = fade.purplepink(not_f)
    pip = ["IP:", "city:", "region:", "loc:", "country:", "postal:", "ISP:"]
    width = 50

    print(f"╔{'═' * width}╗")
    print(f"{RED}{pip[0]}{RESET} {url.get('ip', not_fo)}")
    print(f"{RED}{pip[1]}{RESET} {url.get('city', not_fo)}")
    print(f"{RED}{pip[2]}{RESET} {url.get('region', not_fo)}")
    print(f"{RED}{pip[3]}{RESET} {url.get('loc', not_fo)}")
    print(f"{RED}{pip[4]}{RESET} {url.get('country', not_fo)}")
    print(f"{RED}{pip[5]}{RESET} {url.get('postal', not_fo)}")
    print(f"{RED}{pip[6]}{RESET} {url.get('org', not_fo)}")
    print(f"╚{'═' * width}╝")

    ba = fade.purpleblue("back to home...")
    input(ba)
    os.system('cls' if os.name == 'nt' else 'clear')
    
def phoneluixibouffon():
    n = input("[+] Enter number (+33 XXX): ") or "+33 644637111"
    
    try:
        np = phonenumbers.parse(n)


        if not phonenumbers.is_valid_number(np):
            print("Number is not valid")
            return

        if not phonenumbers.is_possible_number(np):
            print("Number is not possible")
            return

        os.system(f"ignorant {n}")  
        time.sleep(2)  

        cr = phonenumbers.region_code_for_number(np)
        op = carrier.name_for_number(np, "fr")
        em = geocoder.description_for_number(np, "fr")
        fi = phonenumbers.format_number(np, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        fm = phonenumbers.format_number_for_mobile_dialing(np, cr, with_formatting=True)
        tn = phonenumbers.number_type(np)
        tz = timezone.time_zones_for_number(np)
        tz_str = ', '.join(tz)
        
  
        pnum = ["location: ", "region: ", "time Zone: ", "operator: ", "valid Number: ", 
                "possible number: ", "international format: ", "mobile format: ", 
                "original number: ", "E.164 Format: ", "fountry fode: ", "local number: "]
        
        width = 50
        RED = "\033[91m"
        RESET = "\033[0m"

        print(f"╔{'═' * width}╗")
        print("")
        print(f"{RED}{pnum[0]}{RESET}{em}")
        print(f"{RED}{pnum[1]}{RESET}{cr}")
        print(f"{RED}{pnum[2]}{RESET}{tz_str}")
        print(f"{RED}{pnum[3]}{RESET}{op}")
        print(f"{RED}{pnum[4]}{RESET}{str(phonenumbers.is_valid_number(np))}")
        print(f"{RED}{pnum[5]}{RESET}{str(phonenumbers.is_possible_number(np))}")
        print(f"{RED}{pnum[6]}{RESET}{fi}")
        print(f"{RED}{pnum[7]}{RESET}{fm}")
        print(f"{RED}{pnum[8]}{RESET}{str(np.national_number)}")
        print(f"{RED}{pnum[9]}{RESET}{phonenumbers.format_number(np, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"{RED}{pnum[10]}{RESET}{str(np.country_code)}")
        print(f"{RED}{pnum[11]}{RESET}{str(np.national_number)}")
        print("")
        print(f"╚{'═' * width}╝")

        if tn == phonenumbers.PhoneNumberType.MOBILE:
            print("Type: mobile number")
        elif tn == phonenumbers.PhoneNumberType.FIXED_LINE:
            print("Type: fixed line number")
        else:
            print("Type: not Found")
        
        ba = fade.pinkred("back to home...")
        input(ba)
        os.system('cls' if os.name == 'nt' else 'clear')  

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: invalid number format")
    except Exception as e:
        print(f"Error: {str(e)}")

def mail_info():
    e_input = input("[+] enter e-mail address : ") or "google@gmail.com"
  
    email = f"holehe {e_input}"
    os.system(email)
    ba = fade.pinkred("back to home...")
    input(ba)
    os.system('cls' if os.name == 'nt' else 'clear') 



def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        me = "code by ovax | insta banaxou"
        banner = f"""
   ██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗    [small  osint/tool]
   ██║████╗  ██║██╔════╝██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝    1 [IP info]
   ██║██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝     2 [EMAIL info] 
   ██║██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗     3 [NUM info]
   ██║██║ ╚████║██║     ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
   ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
                                                                           | 0 exit |
     {me}
"""

        ban = fade.fire(banner)

        print(ban)
        choice = input("Enter a choice : ")

        if choice == "1":
            ip_info()
        elif choice == "2":
            mail_info()
        elif choice == "3":
            phoneluixibouffon()  
        elif choice == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cowsay -t "code by ovax"')
            time.sleep(3)
            break
        else:
            print("invalid")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

menu()
