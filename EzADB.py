import subprocess
import platform

# define the variables that depends of the OS
if platform.system() == "Windows":
    clearscreen = "cls"
    adb_path = "./windows/adb.exe"
    scrcpy_path = "./windows/scrcpy.exe"
elif platform.system() == "Linux":
    clearscreen = "clear"
    adb_path = "./linux/adb"
    scrcpy_path = "./linux/scrcpy"
elif platform.system() == "Darwin":
    clearscreen = "clear"
    adb_path = "./macos/adb"
    scrcpy_path = "./macos/scrcpy"
else:
    print("Sorry, you are running", platform.system(), "which is not supported by ADB platform tools")
    exit(1)

# start the adb server to allow connection to the device by wifi
def adb_start():
        result = subprocess.run([ adb_path, "start-server"], capture_output=True)
        if result.returncode == 0:
            print("Server started successfully")
        else:
            print("Server failed to start, error:", result.stderr.decode())
# stop the adb server
def adb_stop():
        result = subprocess.run([adb_path, "kill-server"], capture_output=True)
        if result.returncode == 0:
            print("Server stopped successfully")
        else:
            print("Server failed to stop, error:", result.stderr.decode())
# list the devices connected to the adb server/ usb
def adb_devices():
        result = subprocess.run([adb_path, "devices"], capture_output=True)
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print("Failed to get devices, error:", result.stderr.decode())
# installing single file apks
def adb_install():
        apk_path = input("Enter the path of the apk file: ")
        result = subprocess.run([adb_path, "install", apk_path], capture_output=True)
        if result.returncode == 0:
            print("APK installed successfully")
        else:
            print("Failed to install APK, error:", result.stderr.decode())
# installing splitted apks
def adb_install_split():
        apk_base = input("Enter the path of the base APK file: ")
        apk_split_language = input("Enter the path of the language split APK file: ")
        apk_split_arch = input("Enter the path of the architecture split APK file: ")
        apk_split_dpi = input("Enter the path of the DPI split APK file: ")
        result = subprocess.run([adb_path, "install-multiple", apk_base, apk_split_arch, apk_split_language, apk_split_dpi], capture_output=True)
        if result.returncode == 0:
            print("APK installed successfully")
        else:
            print("Failed to install APK, error:", result.stderr.decode())
# uninstalling packages
def adb_uninstall():
    package_name = input("Enter the package name of the app: ")
    result = subprocess.run([adb_path, "uninstall", package_name], capture_output=True) # add some way to check if it's a system app ?
    if result.returncode == 0:
        print("App uninstalled successfully")
    else:
        print("Failed to uninstall app, error:", result.stderr.decode())
# list all the packages installed on the device
#==Broken for the moment, needs a fix==#
def adb_list_packages():
    print(f"\033[{"37;31"}m{"Warning :this feature is broken for the moment and can only print the system packages"}\033[0m")
    input("Press Enter to see package list")
    result = subprocess.run( adb_path, "shell pm list packages", capture_output=True)
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to list packages, error:", result.stderr.decode())
# start scrcpy
def adb_scrcpy():
    result = subprocess.run([scrcpy_path], capture_output=True)
    if result.returncode != 0:
        print("Failed to start SCRCPY, error:", result.stderr.decode())

# main menu
while True:
    subprocess.run([clearscreen], shell=True)
    print("Welcome to EzADB")
    print("1. Start ADB Server")
    print("2. Stop ADB Server")
    print("3. List Devices")
    print("4. Install and uninstall tools")
    print("5. List app packages ")
    print("6. Start SCRCPY")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Starting ADB Server")
        adb_start()
    elif choice == 2:
        print("Stopping ADB Server")
        adb_stop()
    elif choice == 3:
        print("fetching device list")
        adb_devices()
        input("Press Enter to continue")
    elif choice == 4:
        # apk installer and deleter undermenu
        subprocess.run([clearscreen], shell=True)
        print("1. Install single-file APK")
        print("2. Install splitted APK")
        print("3. Uninstall an app")
        print("4. Return to main menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            adb_install()
            input("Press Enter to continue")
        elif choice == 2:
            adb_install_split()
            input("Press Enter to continue")
        elif choice == 3:
            adb_uninstall()
            input("Press Enter to continue")
        elif choice == 4:
            continue
        else:
            print("Invalid choice, please try again")
    elif choice == 5:
        adb_list_packages()
        input("Press Enter to continue")
    elif choice == 6:
        adb_scrcpy()
    elif choice == 7:
        break
    else:
        print("Invalid choice, please try again")