import requests

def admin_scan(target,wordlist):
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"
    with open(wordlist, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        url = target + "/" + line
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            print(green,"Admin page found: ", url,reset)
            break
        else:
            print(red,"Not found: ",url,reset)



if __name__ == '__main__':
    reset = "\033[0m"
    cyan = "\033[36m"
    print(cyan)
    print("""     ___                                  _     ____
    |_ _|_ __  _ __   ___   ___ ___ _ __ | |_  | __ )  ___  _   _
     | || '_ \| '_ \ / _ \ / __/ _ \ '_ \| __| |  _ \ / _ \| | | |
     | || | | | | | | (_) | (_|  __/ | | | |_  | |_) | (_) | |_| |
    |___|_| |_|_| |_|\___/ \___\___|_| |_|\__| |____/ \___/ \__, |
                                     Nothing is Impossible  |___/""")
    print(reset)
    while True:
        print("1. Auto Scan\n2. Manual Scan\n3. Exit")
        ch=input("Select Your Option: ")
        if ch=='1':
            target=input("Enter Your Url [like----> https://www.wordpress.com: ] : ")
            wordlist = "admin_list.txt"
            admin_scan(target,wordlist)
            print()
        if ch=='2':
            target=input("Enter Your Url [like----> https://www.wordpress.com: ] : ")
            wordlist_path=input("Enter Your Wordlist Path : ")
            admin_scan(target, wordlist_path)
            print()
        else:
            break