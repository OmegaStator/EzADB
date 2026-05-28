import subprocess

def devices(fastboot_path):
    result = subprocess.run([fastboot_path, "devices"], capture_output=True)
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to get devices, error:", result.stderr.decode())
    input("Press enter to continue...")

def flash(fastboot_path, flashtype, imgpath):
    result = subprocess([fastboot_path, "flash", flashtype, imgpath])
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to get devices, error:", result.stderr.decode)
    input("Press enter to continue")

def oem_unlock(fastboot_path):
    print("WARNING, THIS WILL FORMAT YOUR DATA PARTITION AND YOU WILL LOOSE ALL DATA")
    input("Press enter to confirm that you backed up all your data and will not blame us for any loss : ")
    print("If the process goes correctly, you will probably need to validate the unlock on your phone")
    result = subprocess.run([fastboot_path, "flashing", "unlock"])
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to unlock bootloader, error:", result.stderr.decode)
        print("Errors on OEM unlocking can come from multiple issues like")
        print("- Device unlocking with a command other than fastboot flashing unlock (some devices use oem unlock)")
        print("- OEM unlock wasn't enabled in device settings")
        print("- OEM unlocking isn't available for your device (check on the bootloader wall of shame)")
    input("Press enter to continue")

def oem_lock(fastboot_path):
    print("WARNING, DON'T RELOCK BOOTLOADER WITHOUT A FULLY STOCK FIRMWARE, OTHERWISE AVB WILL TRIGGER AND YOUR PHONE WON'T BOOT")
    print("THIS WILL ALSO FORMAT DATA")
    input("Press enter to confirm that your firmware is the stock one, that you backed up all your data and will not blame us for any loss : ")
    result = subprocess.run([fastboot_path, "flashing", "unlock"])
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to unlock bootloader, error:", result.stderr.decode)
        print("Errors on OEM unlocking can come from multiple issues like")
        print("- Device locking with a command other than fastboot flashing lock (some devices use oem lock)")
        print("- Signature mismatch between the images and the device (try to flash stock images on both slots)")
    input("Press enter to continue")

