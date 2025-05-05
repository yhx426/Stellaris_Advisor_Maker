# 要求用户输入mod的 英文名字（name_en）和简体中文名字（name_ch）
print("提示：\n1.请确保根目录下存在Config.csv文件\n2.请确保根目录下Res文件夹中已经放置了Config中所配置的音频文件")
name_en = input("请输入mod的英文名字(name_en): ")
name_ch = input("请输入mod的中文名字(name_ch): ")

import os
from datetime import datetime
import csv
import shutil
import logging

# 设置日志格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 创建根文件夹
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
mod_folder = f"sound_mod_{current_time}"
os.makedirs(mod_folder)

# 创建gfx相关文件夹
os.makedirs(os.path.join(mod_folder, "gfx/interface/icons"))

# 创建localisation相关文件夹
os.makedirs(os.path.join(mod_folder, "localisation/english"))
os.makedirs(os.path.join(mod_folder, "localisation/simp_chinese"))

# 创建sound相关文件夹
os.makedirs(os.path.join(mod_folder, "sound/advisor_voice_types"))
os.makedirs(os.path.join(mod_folder, "sound/vo", name_en))

# 英文本地化文件
with open(os.path.join(mod_folder, f"localisation/english/{name_en}_l_english.yml"), "w", encoding="utf-8-sig") as f:
    f.write(f'l_english:\n advisor_{name_en}: "{name_en}"\n')

# 中文本地化文件
with open(os.path.join(mod_folder, f"localisation/simp_chinese/{name_en}_l_simp_chinese.yml"), "w",
          encoding="utf-8-sig") as f:
    f.write(f'l_simp_chinese:\n advisor_{name_en}: "{name_ch}"\n')

# 在sound\advisor_voice_types文件夹中创建文件“advisor_voice_types_{name_en}.txt”
with open(os.path.join(mod_folder, f"sound/advisor_voice_types/advisor_voice_types_{name_en}.txt"), "w",
          encoding="utf-8") as f:
    f.write(f"""advisor_{name_en} = {{
    name = "advisor_{name_en}"
    icon = "gfx/interface/icons/{name_en}.dds"
    playable = {{
        always = yes
    }}
    weight = {{
        base = 0
    }}
}}
""")

# 处理音频文件
root_folder = os.getcwd()
config_file_path = os.path.join(root_folder, "Config.csv")

import chardet

# 检测文件编码
with open(config_file_path, 'rb') as file:
    result = chardet.detect(file.read())
    detected_encoding = result['encoding']

if not os.path.exists(config_file_path):
    logging.error(f"配置文件 {config_file_path} 不存在，请检查文件路径。")
else:
    with open(config_file_path, mode='r', encoding=detected_encoding) as file:
        config_df = list(csv.DictReader(file))


sound_effects = {}
for row in config_df:
    src_file = os.path.join("Res", row["ResFileName"])
    dst_file = os.path.join(mod_folder, f"sound/vo/{name_en}/{row['SoundFile']}_{row['Count']}.wav")

    if not os.path.exists(src_file):
        logging.error(f"源文件 {src_file} 不存在，请检查文件路径或配置表中的文件名。")
    else:
        shutil.copy2(src_file, dst_file)
        logging.info(f"成功复制并重命名为 {dst_file}")

    if row["SoundType"] not in sound_effects:
        sound_effects[row["SoundType"]] = []
    sound_effects[row["SoundType"]].append(row)

# 在sound文件夹下创建文件“{name_en}_effect.asset”
with open(os.path.join(mod_folder, f"sound/{name_en}_effect.asset"), "w", encoding="utf-8") as f:
    for Sound_type, rows in sound_effects.items():
        f.write(f'soundeffect = {{\n    name = {name_en}_{rows[0]["SoundFile"]}\n    sounds = {{\n')
        for row in rows:
            f.write(
                f'        weighted_sound = {{ sound = {name_en}_{row["SoundFile"]}_{row["Count"]} weight = {row["Weights"]} }}\n')
        f.write('    }\n    volume = 0.45\n    max_audible = 1\n    max_audible_behaviour = fail\n}\n')

# 在sound文件夹下创建文件“{name_en}_groups.asset”
with open(os.path.join(mod_folder, f"sound/{name_en}_groups.asset"), "w", encoding="utf-8") as f:
    f.write(f'soundgroup = {{\n    name = advisor_{name_en}\n    soundeffectoverrides = {{\n')
    for Sound_type, sound_files in sound_effects.items():
        f.write(f'        {Sound_type} = {name_en}_{sound_files[0]["SoundFile"]}\n')
    f.write('    }\n}\ncategory = {\n    name = "Voice"\n    soundeffects = {\n')
    for Sound_type, sound_files in sound_effects.items():
        f.write(f'        {name_en}_{sound_files[0]["SoundFile"]}\n')
    f.write('    }\n}\n')

# 在sound文件夹下创建文件“{name_en}_sounds.asset”
with open(os.path.join(mod_folder, f"sound/{name_en}_sounds.asset"), "w", encoding="utf-8") as f:
    for Sound_type, rows in sound_effects.items():
        for row in rows:
            f.write(
                f'sound = {{\n    name = "{name_en}_{row["SoundFile"]}_{row["Count"]}"\n    file = "vo/{name_en}/{row["SoundFile"]}_{row["Count"]}.wav"\n}}\n')

input("已完成音频文件移动 和 配置文件生成\n记得添加Icon和封面资源哦~\n嘀嘀嘀！按任意键启动以太相引擎……")
