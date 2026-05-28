import subprocess

# start the adb server to allow connection to the device by wifi
def start(adb_path):
        result = subprocess.run([ adb_path, "start-server"], capture_output=True)
        if result.returncode == 0:
            print("Server started successfully")
        else:
            print("Server failed to start, error:", result.stderr.decode())
        input("Press enter to continue...")

# stop the adb server
def stop(adb_path):
        result = subprocess.run([adb_path, "kill-server"], capture_output=True)
        if result.returncode == 0:
            print("Server stopped successfully")
        else:
            print("Server failed to stop, error:", result.stderr.decode())
        input("Press enter to continue...")

# list the devices connected to the adb server/ usb
def devices(adb_path):
        result = subprocess.run([adb_path, "devices"], capture_output=True)
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print("Failed to get devices, error:", result.stderr.decode())
        input("Press enter to continue...")

# installing single file apks
def install(adb_path):
        apk_path = input("Enter the path of the apk file: ")
        result = subprocess.run([adb_path, "install", apk_path], capture_output=True)
        if result.returncode == 0:
            print("APK installed successfully")
        else:
            print("Failed to install APK, error:", result.stderr.decode())
        input("Press enter to continue...")

# installing splitted apks
def install_split(adb_path):
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
def uninstall(adb_path):
    package_name = input("Enter the package name of the app: ")
    result = subprocess.run([adb_path, "uninstall", package_name], capture_output=True) # add some way to check if it's a system app ?
    if result.returncode == 0:
        print("App uninstalled successfully")
    else:
        print("Failed to uninstall app, error:", result.stderr.decode())
    input("Press enter to continue...")

# list all the packages installed on the device
def list_packages(adb_path, type):
    # System apps
    if type=="system" or "s":
        result = subprocess.run([adb_path, "shell", "pm", "list", "packages", "-s"], capture_output=True)
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print("Failed to list packages, error:", result.stderr.decode())
    # User apps
    elif type=="user" or "u":
        result = subprocess.run([adb_path, "shell", "pm", "list", "packages", "-3"], capture_output=True)
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            print("Failed to list packages, error:", result.stderr.decode())
    # All apps
    elif type=="all" or "a":
        result = subprocess.run([adb_path, "shell", "pm", "list", "packages"], capture_output=True)
        if result.returncode == 0:
            print(result.stdout.decode())
        else:
            return("Failed to list packages, error:", result.stderr.decode())
    else:
        print("Invalid choice, please try again")
        return

# start scrcpy
def scrcpy(scrcpy_path):
    with open('scrcpy_options.txt') as f:
        options = f.read()
    if options == "":
        result= result = subprocess.run([scrcpy_path],  capture_output=True)
    else:
        result = subprocess.run([scrcpy_path, options],  capture_output=True)
    if result.returncode != 0:
        print("Failed to start SCRCPY, error:", result.stderr.decode())
    else:
        print("SCRCPY started successfully with the following options:", options)
    input("Press Enter to continue...")

# reboot
def reboot(adb_path, reboot_mode):
    result = subprocess.run([ adb_path, "reboot", reboot_mode], capture_output=True)
    if result.returncode == 0:
        print("Device rebooted sucessfully")
    else:
        print("Device failed to reboot, error:", result.stderr.decode())
    input("Press enter to continue...")