from playsound import playsound
import cv2 as cv
import numpy as np
import pyautogui
import time

templates = {
    'armorlv1': {'image': 'armor lv1.png', 'audio': 'armor lv1.wav'},
    'armorlv2': {'image': 'armor lv2.png', 'audio': 'armor lv2.wav'},
    'armorlv3': {'image': 'armor lv3.png', 'audio': 'armor lv3.wav'},
    'armorlv4': {'image': 'armor lv4.png', 'audio': 'armor lv4.wav'},
    'backpack lv1': {'image': 'backpack lv1.png', 'audio': 'backpack lv1.wav'},
    'backpack lv2': {'image': 'backpack lv2.png', 'audio': 'backpack lv2.wav'},
    'backpack lv4': {'image': 'backpack lv4.png', 'audio': 'backpack lv4.wav'},
    'head lv1': {'image': 'head lv1.png', 'audio': 'head lv1.wav'},
    'head lv2': {'image': 'head lv2.png', 'audio': 'head lv2.wav'},
    'head lv3': {'image': 'head lv3.png', 'audio': 'head lv3.wav'},
    'head lv4': {'image': 'head lv4.png', 'audio': 'head lv4.wav'},
    'knock shield lv1': {'image': 'knock shield lv1.png', 'audio': 'knock shield lv1.wav'},
    'knock shield lv2': {'image': 'knock shield lv2.png', 'audio': 'knock shield lv2.wav'},
    'knock shield lv3': {'image': 'knock shield lv3.png', 'audio': 'knock shield lv3.wav'},
    'knock shield lv4': {'image': 'knock shield lv4.png', 'audio': 'knock shield lv4.wav'},
    'need ammo energy': {'image': 'need ammo energy.png', 'audio': 'need ammo energy.wav'},
    'need ammo heavy': {'image': 'need ammo heavy.png', 'audio': 'need ammo heavy.wav'},
    'need ammo light': {'image': 'need ammo light.png', 'audio': 'need ammo light.wav'},
    'need ammo shotgun': {'image': 'need ammo shotgun.png', 'audio': 'need ammo shotgun.wav'},
    'need ammo sniper': {'image': 'need ammo sniper.png', 'audio': 'need ammo sniper.wav'},
    'need batt': {'image': 'need batt.png', 'audio': 'need batt.wav'},
    'need cell': {'image': 'need cell.png', 'audio': 'need cell.wav'},
    'need med': {'image': 'need med.png', 'audio': 'need med.wav'},
    'need phx': {'image': 'need phx.png', 'audio': 'need phx.wav'},
    'need syring': {'image': 'need syring.png', 'audio': 'need syring.wav'},
    'need up barrel': {'image': 'need up barrel.png', 'audio': 'need up barrel.wav'},
    'need up hopup': {'image': 'need up hopup.png', 'audio': 'need up hopup.wav'},
    'need up mag': {'image': 'need up mag.png', 'audio': 'need up mag.wav'},
    'need up optic': {'image': 'need up optic.png', 'audio': 'need up optic.wav'},
    'need up stock': {'image': 'need up stock.png', 'audio': 'need up stock.wav'},
    'need weapon': {'image': 'need weapon.png', 'audio': 'need weapon.wav'},
    'nice': {'image': 'nice.png', 'audio': 'nice.wav'},
    'quote1 (nice1)': {'image': 'quote1.png', 'audio': 'quote1.wav'},
    'quote2 (not jp1)': {'image': 'quote2.png', 'audio': 'quote2.wav'},
    'quote3 (nice2)': {'image': 'quote3.png', 'audio': 'quote3.wav'},
    'quote4 (not jp1)': {'image': 'quote4.png', 'audio': 'quote4.wav'},
    'quote5 (thank)': {'image': 'quote5.png', 'audio': 'quote5.wav'},
    'quote7 (thank2)': {'image': 'quote7.png', 'audio': 'quote7.wav'},
    'some one has been here': {'image': 'some one has been here.png', 'audio': 'some one has been here.wav'},
    'ult': {'image': 'ult.png', 'audio': 'ult.wav'},
    'watch there': {'image': 'watch there.png', 'audio': 'watch there.wav'},
    'attack': {'image': 'attack.png', 'audio': 'attack.wav'},
    'enemy ': {'image': 'enemy.png', 'audio': 'enemy .wav'},
    'going here': {'image': 'going here.png', 'audio': 'going here.wav'},
    'def here': {'image': 'def here.png', 'audio': 'def here.wav'},
    'loot here': {'image': 'loot here.png', 'audio': 'loot here.wav'}
}

# Load the template images
for template in templates.values():
    template_raw = cv.imread(template['image'], cv.IMREAD_GRAYSCALE)
    template['image'] = cv.convertScaleAbs(template_raw)
    time.sleep(0.3)

# Set the desired width and height of the screenshot
width, height = 1820, 1000

# Loop to capture frames and perform template matching
while True:
    # Capture a screenshot of the game screen
    screenshot = pyautogui.screenshot(region=(0, 0, width, height))
    frame = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Perform template matching for each template
    for template_name, template in templates.items():
        mat = cv.matchTemplate(frame_gray, template['image'], cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(mat)

        # Check if the maximum correlation value is above the threshold
        if max_val >= 0.95:
            print(f'Found {template_name}. Best match confident: {max_val}')
            playsound(template['audio'])

    # Delay to control the frame rate
    time.sleep(0.3)
