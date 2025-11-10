import platform
import subprocess

def fastboot_init():
    if platform.system() == "Windows":
        fastboot_path = "./windows/fastboot"
    elif platform.system() == "Linux":
        fastboot_path = "./linux/fastboot"
    elif platform.system() == "Darwin":
        fastboot_path = "./macos/fastboot"

def fastboot_devices():
    result = subprocess.run([fastboot_path, "devices"], capture_output=True)
    if result.returncode == 0:
        return(result.stdout.decode())
    else:
        return("Failed to get devices, error:", result.stderr.decode())
    input("Press enter to continue...")

print("HEY YOU,YES YOU !")
print("This file is a library for EzADB, if you want to use it, please run EzADB and select 7. Switch to EzFastboot")