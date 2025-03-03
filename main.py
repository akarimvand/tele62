import os
import subprocess

def install_requirements():
    try:
        # بررسی وجود فایل requirements.txt
        if os.path.exists("requirements.txt"):
            print("Installing required packages...")
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("All packages installed successfully.")
        else:
            print("requirements.txt not found!")
    except Exception as e:
        print(f"Error installing packages: {e}")

if __name__ == "__main__":
    install_requirements()
