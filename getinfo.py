import inspect
import subprocess



print(
"""\n
 888888   .d8888b.                 .d8888b.   .d8888b.   d888    d888   
    88b  d88P  Y88b               d88P  Y88b d88P  Y88b d8888   d8888   
     888 888    888                    .d88P      .d88P   888     888   
     888 888    888 888  888  888     8888       8888     888     888   
     888 888    888 888  888  888       Y8b.       Y8b.   888     888   
     888 888    888 888  888  888 888    888 888    888   888     888   
     88P Y88b  d88P Y88b 888 d88P Y88b  d88P Y88b  d88P   888     888   
     888   Y8888P    Y8888888P     Y8888P     Y8888P   8888888 8888888 
   .d88P                                                                
 .d88P                                                                
888P \n""")

print("Welcome to Get-Fast")
print("Tool created by: Joel Leiton\n")

print("Please select an option that you want run\n")

while True:
    print("1) Basic System Information")
    print("2) Get Wifi Passwords")
    print("3) Basic Local User Information")
    print("4) Exit Program")

    choice = input("Enter choice: ")
    choice = choice.strip()

    if (choice == '1'):
        with open('sysinfo.txt', 'w') as f:
            results = subprocess.run(['systeminfo'], stdout=f, stderr=subprocess.PIPE, text=True)
            resultconsole = subprocess.run(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(resultconsole.stdout) 

    elif (choice == '2'):
        getwf = subprocess.run(['netsh', 'wlan', 'show', 'profile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(getwf.stdout)

        print('Now write the network that you want the password')
        net=input('Selecting network....')

        getwf = subprocess.run(['netsh', 'wlan', 'show', 'profile', f"name={net}", 'key=clear'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        with open('Wifiobtain.txt', 'w') as f:
            results = subprocess.run(['netsh', 'wlan', 'show', 'profile', f"name={net}", 'key=clear'], stdout=f, stderr=subprocess.PIPE, text=True)
        print(getwf.stdout)

    elif (choice == '3'):
        usersinf = subprocess.run(['net', 'user'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(usersinf.stdout) 

        print('Now write the user to obtain more information')
        us=input('Selecting user....')

        with open('Userinfo.txt', 'w') as f:
            getus = subprocess.run(['net', 'user', f'{us}'], stdout=f, stderr=subprocess.PIPE, text=True)
            getus = subprocess.run(['net', 'user', f'{us}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(getus.stdout)
    
    elif (choice == '4'):
        break
    else:
        print('Invalid Option. Please try again.')
