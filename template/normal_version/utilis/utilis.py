import pyautogui
import PIL
import pytesseract as ptr
import romajitable
import urllib
import requests
import cv2 as cv
import numpy as np


def image_processing(
    file_path_screenshot, 
    file_path_screenshot_adjusted, 
    config, 
    alpha, 
    beta,
    image_processing_choice
):
    # Take a full screenshot
    pyautogui.screenshot(imageFilename=file_path_screenshot)
    
    # If user chooses to use OpenCV for image processing, the following script will execute
    if image_processing_choice == "1":
        # Open image and store it as variable
        img = cv.imread(file_path_screenshot)
        # Convert image to grayscale
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Increase contrast
        adjusted_image = cv.convertScaleAbs(img_gray, alpha=alpha)
        # Increase highlights
        adjusted_image = cv.addWeighted(adjusted_image, 1, np.zeros_like(adjusted_image), 0, beta)
        # Save the adjusted image
        cv.imwrite(file_path_screenshot_adjusted, adjusted_image)

    # If user chooses to convert the image only into grayscale, the following script will execute.
    elif image_processing_choice == "2":
        img_rgb = PIL.Image.open(file_path_screenshot).convert("L")
        img_rgb.save(file_path_screenshot_adjusted)
        
    # Extract text from image using pytesseract    
    extracted_text = ptr.image_to_string(
        PIL.Image.open(file_path_screenshot_adjusted), config=config
    )
    return extracted_text

# Function to read a config and return it
def read_config(file_path_config):
    with open(file_path_config, "r") as config_file:
        for line in config_file:
            line = line.strip()
            if line.startswith("voice_vox_text_to_speech_model:"):
                voice_vox_text_to_speech_model = line[31:]
            elif line.startswith("image_processing_choice:"):
                image_processing_choice = line[24:]
    return voice_vox_text_to_speech_model, image_processing_choice


# Function to create a text-to-speech file using voicevox engine
def create_voicevox_text_to_speech_file(
    text, 
    voice_vox_text_to_speech_model, 
    file_path_JP_Voice,
):
    # Turn some of the answer that have a english text to katakana text for example
    # If answer_jp contain a word "apple" it'll turn it to "appuru"
    result = romajitable.to_kana(text)
    katakaned = result.katakana

    # Text-to-speech part (make sure you have open VOICEVOX.exe)
    voicevox_url = "http://localhost:50021"
    params_encoded = urllib.parse.urlencode(
        {"text": katakaned, "speaker": voice_vox_text_to_speech_model}
    )
    request = requests.post(f"{voicevox_url}/audio_query?{params_encoded}")
    params_encoded = urllib.parse.urlencode(
        {
            "speaker": voice_vox_text_to_speech_model,
            "enable_interrogative_upspeak": True,
        }
    )
    request = requests.post(
        f"{voicevox_url}/synthesis?{params_encoded}", json=request.json()
    )
    with open(file_path_JP_Voice, "wb") as outfile:
        outfile.write(request.content)
        outfile.close()