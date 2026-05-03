import subprocess
import platform     # OS Detection mechanism
from lib import EzADBLib as adb
from lib import EzFastboot as fb


## define the variables that depends of the OS
if platform.system() == "Windows":
    clearscreen = "cls"
    adb_path = "./windows/adb.exe"
    scrcpy_path = "./windows/scrcpy.exe"
    fastboot_path = "./windows/fastboot"
elif platform.system() == "Linux":
    clearscreen = "clear"
    adb_path = "./linux/adb"
    scrcpy_path = "./linux/scrcpy"
    fastboot_path = "./linux/fastboot"
elif platform.system() == "Darwin":
    clearscreen = "clear"
    adb_path = "./macos/adb"
    scrcpy_path = "./macos/scrcpy"
    fastboot_path = "./macos/fastboot"
else:
    print("Sorry, you are running", platform.system(), "which is not supported by ADB platform tools")
    exit(1)


## ADB menu
def adb_menu():
    subprocess.run([clearscreen], shell=True)
    print("Welcome to EzADB")
    print("A. Start ADB Server")
    print("K. Stop ADB Server")
    print("D. List Devices")
    print("I. Install and uninstall tools")
    print("L. List app packages ")
    print("S. Start SCRCPY")
    print("F. Switch to EzFastboot")

    choice = int(input("Enter your choice: "))
    
    if choice == "a" or "A":
        print("Starting ADB Server...")
        adb.start(adb_path)
    elif choice == "k" or "K":
        print("Stopping ADB Server...")
        adb.stop(adb_path)
    elif choice == "d" or "D":
        print("Fetching device list...")
        adb.devices(adb_path)
    elif choice == "i" or "I":
        # apk installer and deleter submenu
        subprocess.run([clearscreen], shell=True)
        print("I. Install single-file APK")
        print("S. Install splitted APK")
        print("U. Uninstall an app")
        print("E. Return to main menu")
        choice = int(input("Enter your choice: "))
        if choice == "i" or "I":
            adb.install(adb_path)
            input("Press Enter to continue")
        elif choice == "s" or "S":
            adb.install_split(adb_path)
            input("Press Enter to continue")
        elif choice == "u" or "U":
            adb.uninstall(adb_path)
            input("Press Enter to continue")
        elif choice == "e" or "E":
            return
        else:
            print("Invalid choice, please try again")
    elif choice == "l" or "L" :
        choice = input("What package type do you want to list ? (system, user, all): ")
        adb.list_packages(choice)
        input("Press Enter to continue")
    elif choice == "s" or "S":
        adb.scrcpy(scrcpy_path)
    elif choice == "f" or "F":
        fastboot_menu()
    else:
        print("Invalid choice, please try again")
        input("Press enter continue...")

# Fastboot menu
def fastboot_menu():
    print("D. List fastboot devices")
    print("E. Switch to EzADB")
    fbchoice = input("Enter your choice: ")
    if fbchoice == "d" or "D":
            fb.devices(fastboot_path)
    elif fbchoice == "e" or "E":
        return
    else:
        print(fbchoice, choice)
    input("Press enter to continue")

# Main loop
while True:
    adb_menu()