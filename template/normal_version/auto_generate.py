import os
from utilis.utilis import create_voicevox_text_to_speech_file, read_config

directory_path = os.path.dirname(os.path.realpath(__file__))
file_path_config = directory_path + r"config.txt"

file_dic = {
    "KEYS": {
        "file_name": ".wav", 
        "JP_sentence": ""
    },
}

for keys in file_dic:
    voice_vox_text_to_speech_model, image_processing_choice= read_config(file_path_config)
    generated = file_dic[keys]
    create_voicevox_text_to_speech_file(
        generated["JP_sentence"], voice_vox_text_to_speech_model, generated["file_name"]
    )
