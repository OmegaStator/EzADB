import subprocess

def devices(fastboot_path):
    result = subprocess.run([fastboot_path, "devices"], capture_output=True)
    if result.returncode == 0:
        print(result.stdout.decode())
    else:
        print("Failed to get devices, error:", result.stderr.decode())
    input("Press enter to continue...")

