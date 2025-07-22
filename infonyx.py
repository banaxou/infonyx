# code by ovax 
import os
import time
import fade
import requests
import subprocess
import phonenumbers
import json
from phonenumbers import carrier, geocoder, timezone

R = "\033[91m"
r = "\033[0m"

def ip_info():
    ipl = input(f"[{R}+{r}] Enter IP: ")
    print("")
    url = requests.get(f"https://ipinfo.io/{ipl}/json").json()
    not_f = "not found"
    pip = ["IP:", "Hostname:", "City:", "Region:", "Location:", "Country:", "Postal:", "ISP:", "Time zone:", "Anycast", "Open Ports:"]
    keys = ["ip", "hostname", "city", "region", "loc", "country", "postal", "org", "timezone", "anycast"]
    urlx = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-ip?ip={ipl}"
    res = requests.get(urlx)
    width = 50

    print(f"╔{'═' * width}╗")
    info = {}
    for i in range(len(keys)):
        value = url.get(keys[i], not_f)
        info[keys[i]] = value
        print(f" {R}{pip[i]}{r} {value} ")
    print(f"╚{'═' * width}╝")

    d = str(input("Do you want to check if data is compromised and scan IP port? (y/n) :")).strip().lower()
    
    if d == "y":
        if res.status_code == 200:
            try:
                data = res.json()

                if 'stealers' in data and not data['stealers']:
                    print("data has not compromised")
                else:
                    print("status code:", res.status_code)
                    print(f"╔{'═' * width}╗")
                    print(json.dumps(data, indent=2))
                    print(f"╚{'═' * width}╝")

            except ValueError:
                print("no response json")

        elif res.status_code != 200:
            print("Error request")
            # menu()  

        print(f"╔{'═' * width}╗")
        print("port scan.. ▼")
        open_p = []
        try:
            nmapx = subprocess.run(["nmap", "-p-", "--open", ipl], capture_output=True, text=True).stdout
            lines = nmapx.split("\n")
            for line in lines:
                if "/tcp" in line and "open" in line:
                    port = line.split("/")[0].strip()
                    open_p.append(port)
        except Exception as e:
            open_p = ["nmap error"]

        open_pd = ', '.join(map(str, open_p)) if open_p else "None"
        print(f" {R}{pip[-1]}{r} {open_pd} ")
        print(f"╚{'═' * width}╝")

        info["port"] = open_p

    elif d == "n" or d == "":
        print("back to home...")

    ajson = f"ip_{ipl}.json"
    with open(ajson, "w", encoding="utf-8") as jsson:
        json.dump(info, jsson, ensure_ascii=False, indent=4)

    input("press enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


def phoneluixibouffon():
    n = input(f"[{R}+{r}] Enter number (+33 XXX): ") or "+33 0644637111"
    
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

        pnum = [
            "location: ", "region: ", "time Zone: ", "operator: ", 
            "valid Number: ", "possible number: ", "international format: ", 
            "mobile format: ", "original number: ", "E.164 Format: ", 
            "country code: ", "local number: ", "type: "
        ]
        width = 50

        print(f"╔{'═' * width}╗")
        print("")
        print(f" {R}{pnum[0]}{r}{em} ")
        print(f" {R}{pnum[1]}{r}{cr} ")
        print(f" {R}{pnum[2]}{r}{tz_str} ")
        print(f" {R}{pnum[3]}{r}{op} ")
        print(f" {R}{pnum[4]}{r}{str(phonenumbers.is_valid_number(np))} ")
        print(f" {R}{pnum[5]}{r}{str(phonenumbers.is_possible_number(np))} ")
        print(f" {R}{pnum[6]}{r}{fi} ")
        print(f" {R}{pnum[7]}{r}{fm} ")
        print(f" {R}{pnum[8]}{r}{str(np.national_number)} ")
        print(f" {R}{pnum[9]}{r}{phonenumbers.format_number(np, phonenumbers.PhoneNumberFormat.E164)} ")
        print(f" {R}{pnum[10]}{r}{str(np.country_code)} ")
        print(f" {R}{pnum[11]}{r}{str(np.national_number)} ")

        if tn == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {R}{pnum[12]}{r}mobile number")
        elif tn == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {R}{pnum[12]}{r}fixed line number")
        else:
            print(f" {R}{pnum[12]}{r}not found")
        
        print("")
        print(f"╚{'═' * width}╝")
        ba = fade.pinkred("back to home...")
        input(ba)
        os.system('cls' if os.name == 'nt' else 'clear')  

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: invalid number format")
    
    except Exception as e:
        print(f"Error: {str(e)}")

def mail_info():
    e_input = input(f"[{R}+{r}] enter e-mail address : ") or "google@gmail.com"
  
    email = f"holehe {e_input}"
    os.system(email)
    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={e_input}"
    res = requests.get(url)  
    if res.status_code == 200:
        try:
            data = res.json()

            if 'message' in data and "not associated with a computer infected" in data['message']:
                print("data has not compromised")
            else:
                print("status code: ", res.status_code)
                print(json.dumps(data, indent=2))
        except ValueError :
            print("no response json")
    elif res.status_code != 200:
        print("Error request")
        
    ba = fade.pinkred("back to home...")
    input(ba)
    os.system('cls' if os.name == 'nt' else 'clear') 



def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        me = "code by ovax | insta banaxou"
        vs = fade.greenblue("v1.3.1")     
        banner = f"""                                           
   ██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗    
   ██║████╗  ██║██╔════╝██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝     1 : IP info
   ██║██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝      2 : EMAIL info 
   ██║██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗      3 : NUM info
   ██║██║ ╚████║██║     ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗     
   ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝     {vs}{r}
                                                                           | 0 exit |
     {me}
"""

        ban = fade.fire(banner)

        print(ban)
        choice = input(f"{R}>{r} enter a choice: ")

        if choice == "1":
            ip_info()
        elif choice == "2":
            mail_info()
        elif choice == "3":
            phoneluixibouffon()  
        elif choice == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cowsay -t "code by ovax "infonyx +" soon "')
            time.sleep(3)
            break
        else:
            print("invalid")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

menu()
