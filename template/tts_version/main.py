import keyboard
import os
import winsound
import random
from playsound import playsound
from utilis.condition import condition_dic
from utilis.utilis import (
    create_voicevox_text_to_speech_file, 
    read_config, 
    image_processing, 
    play_text_to_speech_file
)


# Constance for contrast and highligh value to use with openCV
ALPHA = 1
BETA = 0

CONFIG = r"--psm 11 --oem 3"

# File path
directory_path = os.path.dirname(os.path.realpath(__file__))
file_path_JP_Voice = directory_path + r"\temp\JP_Voice.wav"
file_path_config = directory_path + r"\config.txt"
file_path_screeeshot = directory_path + r"\temp\screeeshot.png"
file_path_screeeshot_adjusted = directory_path + r"\temp\screeeshot_grayscale.png"
 
# Use read_config function to read config from the file and store it as variable
voice_vox_text_to_speech_model, image_processing_choice = read_config(file_path_config)

capturing = False

playsound(directory_path + r"\test.wav")

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
                    # Alert user with window default alert sound
                    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

                    # Convert the set to a list before using random.choice
                    converted = list(matched_condition)
                    
                    # Use random.choice to select a random phrase
                    final_text = random.choice(converted)
                    
                    create_voicevox_text_to_speech_file(
                        final_text,
                        voice_vox_text_to_speech_model,
                        file_path_JP_Voice,
                    )
                    play_text_to_speech_file(file_path_JP_Voice)

            # Check if the 'v' key is released to stop capturing
            if not keyboard.is_pressed("v"):
                # Unblock the 'v' key
                keyboard.unblock_key("v")
                capturing = False  # Reset the flag to stop capturing
                print("Stopped capturing.\n-----------------------")
                break


while True:
    check_condition()
