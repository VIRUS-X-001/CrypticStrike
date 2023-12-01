import os
import pyfiglet
import subprocess
import time
import whois
import requests
from bs4 import BeautifulSoup

def install_required_libraries():
    try:
        subprocess.check_call(['pip', 'install', 'requests'])
        subprocess.check_call(['pip', 'install', 'pyfiglet'])
        subprocess.check_call(['pip', 'install', 'python-whois'])
        subprocess.check_call(['pip', 'install', 'beautifulsoup4'])
    except Exception as e:
        print(f"Error installing libraries: {e}")

def get_whois_data(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_web_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_whois_data(whois_data):
    print("\033[1;32m[+] Whois Data:\033[1;31m")
    print(f"\033[1;31mDomain:\033[1;31m {whois_data.domain_name}")
    print(f"\033[1;31mRegistrar:\033[1;31m {whois_data.registrar}")
    print(f"\033[1;31mCreation Date:\033[1;32m {whois_data.creation_date}")
    print(f"\033[1;31mExpiration Date:\033[1;32m {whois_data.expiration_date}")
    print(f"\033[1;31mEmails:\033[1;32m {whois_data.emails}")
    print(f"\033[1;31mPhone Numbers:\033[1;32m {whois_data.phone}")
    print(f"\033[1;31mName Servers:\033[1;32m {whois_data.name_servers}")
    print(f"\033[1;31mRegistrant Name:\033[1;32m {whois_data.name}")
    print(f"\033[1;31mRegistrant Organization:\033[1;32m {whois_data.org}")
    print(f"\033[1;31mRegistrant Email:\033[1;32m {whois_data.email}")
    print(f"\033[1;31mRegistrant Phone:\033[1;32m {whois_data.phone}")

def print_web_content(title, url):
    print("\033[1;32m[+] Web Content:\033[1;32m")
    print(f"\033[1;33mPage Title:\033[1;32m {title}")
    print(f"\033[1;33mURL:\033[1;32m {url}")

def beautify_output():
    print("=================================================")

# Install required libraries
install_required_libraries()
os.system('clear')
while True:
    text = pyfiglet.figlet_format("Cryptic Strike", font="graffiti")
    print("\033[1;97m" + text)
    print("")
    print("")
    text = "[#] These tools are programmed by (VIRUS-X-001)\n \n"
    for char in text:
        print("\033[1;97m" +char, end='', flush=True)
        time.sleep(0.1)
    print("")
    print("")
    domain = input("\033[1;96mEnter the target URL (or 'q' to quit):-\033[0m")
    if domain.lower() == 'q':
        break

    whois_data = get_whois_data(domain)

    if whois_data:
        beautify_output()
        print_whois_data(whois_data)
    else:
        print("\033[1;31mFailed to retrieve Whois data.\033[1;32m")

    url = domain
    web_content = get_web_content(url)

    if web_content:
        soup = BeautifulSoup(web_content, 'html.parser')
        title = soup.title.text.strip()
        beautify_output()
        print_web_content(title, url)
    else:
        print("\033[1;31mFailed to retrieve web content.\033[1;32m")

    choice = input("\n\033[1;34mDo you want to continue? (Y/N):\033[0m ")
    if choice.lower() != 'y':
        break
