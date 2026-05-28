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
    print("1. Start ADB Server")
    print("2. Stop ADB Server")
    print("3. List Devices")
    print("4. Install and uninstall tools")
    print("5. List app packages ")
    print("6. Start SCRCPY")
    print("7. Reboot to a specific mode")
    print("8. Switch to EzFastboot")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Starting ADB Server...")
        adb.start(adb_path)
    elif choice == 2:
        print("Stopping ADB Server...")
        adb.stop(adb_path)
    elif choice == 3:
        print("Fetching device list...")
        adb.devices(adb_path)
    elif choice == 4:
        # apk installer and deleter submenu
        subprocess.run([clearscreen], shell=True)
        print("1. Install single-file APK")
        print("2. Install splitted APK")
        print("3. Uninstall an app")
        print("4. Return to main menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            adb.install(adb_path)
            input("Press Enter to continue")
        elif choice == 2:
            adb.install_split(adb_path)
            input("Press Enter to continue")
        elif choice == 3:
            adb.uninstall(adb_path)
            input("Press Enter to continue")
        elif choice == 4:
            return
        else:
            print("Invalid choice, please try again")
    elif choice == 5 :
        choice = input("What package type do you want to list ? (system, user, all): ")
        adb.list_packages(choice)
        input("Press Enter to continue")
    elif choice == 6:
        adb.scrcpy(scrcpy_path)
    elif choice == 7:
        print("What mode do you want your phone to reboot into")
        print("1. Reboot to system (normal mode)")
        print("2. Reboot to system (Safe mode)")
        print("3. Reboot to recovery")
        print("4. Reboot to fastboot / download mode")
        rbchoice = int(input("What mode do you want to reboot to : "))
        if rbchoice == 1:
            adb.reboot(adb_path, "")
        elif rbchoice == 2:
            adb.reboot(adb_path, "safe")
        elif rbchoice == 3:
            adb.reboot(adb_path, "recovery")
        elif rbchoice == 4:
            adb.reboot(adb_path, 'bootloader')
        else:
            print("Invalid choice")
            input("Press enter continue...")
    elif choice == 8:
        fastboot_menu()
    else:
        print("Invalid choice, please try again")
        input("Press enter continue...")

# Fastboot menu
def fastboot_menu():
    print("1. List fastboot devices")
    print("2. Unlock Bootloader")
    print("3. Relock Bootloader")
    print('4. Flash a partition')
    print("5. Switch to EzADB")
    fbchoice = int(input("Enter your choice: "))
    if fbchoice == 1:
        fb.devices(fastboot_path)
    elif fbchoice == 2:
        fb.oem_unlock(fastboot_path)
    elif fbchoice == 3:
        fb.oem_lock(fastboot_path)
    elif fbchoice == 4:
        partition = input("What partition do you want to flash (name needs to be in lower case) : ")
        imgfile = input("Please enter the path to the file you want to flash (Is a .img in most cases, might be a .efi for custom bootloaders)")
        fb.flash(fastboot_path, partition)
    elif fbchoice == 5:
        return
    else:
        print(fbchoice, choice)
    input("Press enter to continue")

# Main loop
while True:
    adb_menu()