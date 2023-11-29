import os
from utilis.utilis import create_voicevox_text_to_speech_file, read_config

directory_path = os.path.dirname(os.path.realpath(__file__))
file_path_config = directory_path + r"config.txt"

file_dic = {
    "HELMET": {
        "file_name": "equipment_helmet.wav", 
        "JP_sentence": "ヘルメットが欲しいです"
    },
    "BODY SHIELD": {
        "file_name": "equipment_body_shield.wav",
        "JP_sentence": "アーマーが欲しいです",
    },
    "KNOCKDOWN SHIELD": {
        "file_name": "equipment_knockdown_shield.wav",
        "JP_sentence": "ノックダウンシールドが欲しいです",
    },
    "BACKPACK": {
        "file_name": "equipment_backpack.wav", 
        "JP_sentence": "バックパックが欲しいです"
    },
    "PHOENIX KIT": {
        "file_name": "item_phoenix_kit.wav", 
        "JP_sentence": "フェニックが欲しいです"
    },
    "SHIELD BATTERY": {
        "file_name": "item_shield_battery.wav",
        "JP_sentence": "バッテリーが欲しいです",
    },
    "MED KIT": {
        "file_name": "item_med_kit.wav", 
        "JP_sentence": "メディキットが欲しいです"
    },
    "SHIELD CELL": {
        "file_name": "item_shield_cell.wav", 
        "JP_sentence": "シールドセルが欲しいです"
    },
    "ENERGY AMMO": {
        "file_name": "ammo_energy.wav", 
        "JP_sentence": "エナジーアモが欲しいです"
    },
    "HEAVY ROUNDS": {
        "file_name": "ammo_heavy.wav", 
        "JP_sentence": "ヘビーラウンズが欲しいです"
    },
    "LIGHT ROUNDS": {
        "file_name": "ammo_light.wav", 
        "JP_sentence": "ライトラウンズが欲しいです"
    },
    "SHOTGUN SHELLS": {
        "file_name": "ammo_shotgun.wav",
        "JP_sentence": "ショットガンシェルが欲しいです",
    },
    "SNIPER AMMO": {
        "file_name": "ammo_sniper.wav", 
        "JP_sentence": "スナイパーアモが欲しいです"
    },
    "BARREL ATTACHMENT SLOT": {
        "file_name": "attachment_barrel.wav",
        "JP_sentence": "バレルが欲しいです",
    },
    "MAG ATTACHMENT SLOT": {
        "file_name": "attachment_mag.wav",
        "JP_sentence": "マガジンが欲しいです",
    },
    "OPTIC ATTACHMENT SLOT": {
        "file_name": "attachment_optic.wav",
        "JP_sentence": "オプティックが欲しいです",
    },
    "HOP UP ATTACHMENT SLOT": {
        "file_name": "attachment_hop_up.wav",
        "JP_sentence": "ホップアップが欲しいです",
    },
    "AVOID THIS AREA": {
        "file_name": "ping_avoid_this_area.wav",
        "JP_sentence": "このエリアは避けた方がいいです",
    },
    "ENEMY AUDIO": {
        "file_name": "ping_enemy_audio.wav", 
        "JP_sentence": "敵の音がします"
    },
    "LOOTING THIS AREA": {
        "file_name": "ping_looting_this_area.wav",
        "JP_sentence": "このエリアでアイテムを拾っています",
    },
    "ATTACK HERE": {
        "file_name": "ping_attack_here.wav", 
        "JP_sentence": "ここを攻撃してください"
    },
    "REGROUP HERE": {
        "file_name": "ping_regroup_here.wav",
        "JP_sentence": "ここで再集結してください",
    },
    "DEFEND HERE": {
        "file_name": "ping_defend_here.wav", 
        "JP_sentence": "ここを守ってください"
    },
    "WATCHING HERE": {
        "file_name": "ping_watching_here.wav",
        "JP_sentence": "ここを見張っています",
    },
    "SOMEONE'S BEEN HERE": {
        "file_name": "ping_someone's_been_here.wav",
        "JP_sentence": "誰かがここにいました",
    },
    "NICE": {
        "file_name": "emote_nice.wav", 
        "JP_sentence": "ありがとうです"
    },
}

for keys in file_dic:
    voice_vox_text_to_speech_model, image_processing_choice= read_config(file_path_config)
    generated = file_dic[keys]
    create_voicevox_text_to_speech_file(
        generated["JP_sentence"], voice_vox_text_to_speech_model, generated["file_name"]
    )
