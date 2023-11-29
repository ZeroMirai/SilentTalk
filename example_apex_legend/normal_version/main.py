import keyboard
import os
from playsound import playsound
from utilis.condition import condition_dic
from utilis.utilis import image_processing, read_config

# Constance for contrast and highligh value to use with openCV
ALPHA = 1
BETA = 0

CONFIG = r"--psm 11 --oem 3"

# File path
directory_path = os.path.dirname(os.path.realpath(__file__))
file_path_screeeshot = directory_path + r"\temp\screeeshot.png"
file_path_screeeshot_adjusted = directory_path + r"\temp\screeeshot_adjusted.png"
file_path_config = directory_path + r"\config.txt"

# Use read_config function to read config from the file and store it as variable
voice_vox_text_to_speech_model, image_processing_choice = read_config(file_path_config)

capturing = False

playsound(directory_path + r"\voice\test.wav")

def check_condition():
    global capturing
    print("\n\n*----------*----------*\nPress 'v' to start capturing...")

    while True:
        if keyboard.is_pressed("v"):
            # Disable the 'v' key to prevent repeated recording trigger
            keyboard.block_key("v")
            capturing = True
            print("Capturing...")

        if capturing:
            # Image processing and extract text from image
            text = image_processing(
                file_path_screeeshot, 
                file_path_screeeshot_adjusted, 
                CONFIG, 
                ALPHA, 
                BETA,
                image_processing_choice
            )
            # If the extracted text is inside the condition, it would execute the script
            for keys in condition_dic:
                if keys in text:
                    matched_condition = condition_dic[keys]
                    print(f"Found {keys}")
                    playsound(directory_path + matched_condition["audio"])
                    
            # Check if the 'v' key is released to stop capturing
            if not keyboard.is_pressed("v"):
                # Unblock the 'v' key
                keyboard.unblock_key("v")
                capturing = False  # Reset the flag to stop capturing
                print("Stopped capturing.\n-----------------------\n")
                break


while True:
    check_condition()
