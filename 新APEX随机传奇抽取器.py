import random
string_list = ['艾许', '疯麻吉', '弹道', '班加罗尔', '暴雷', '变幻', '地平线', '亡灵', '恶灵', '动力小子', '探路者', '密客', '寻血猎犬', '瓦尔基里', '希尔',
               '万蒂奇', '催化剂', '侵蚀', '兰伯特', '沃特森', '导管', '直布罗陀', '命脉', '罗八', '幻象', '纽卡斯尔']

# 确保不重复选中英雄
selected_heroes = random.sample(string_list, 3)  # 随机选择3个不重复的名字
print(f"这把需要选用的阵容是: {selected_heroes[0]}， {selected_heroes[1]}， {selected_heroes[2]}")

# answer = random.choice(string_list)
# answer2 = random.choice(string_list)
# answer3 = random.choice(string_list)
# print(f"这把需要选用的阵容是: {answer}， {answer2}， {answer3}")

str_gun = ["电能子弹", "重型子弹", "轻型子弹", "狙击子弹", "霰弹子弹"]
str_gun2 = ["电能子弹", "重型子弹", "轻型子弹", "狙击子弹", "霰弹子弹"]

selected_guns = []

for i in range(3):
    random_gun = random.choice(str_gun)
    random_gun2 = random.choice(str_gun2)
    selected_guns.append((random_gun, random_gun2))  # 将选中的武器添加到列表中
print(f"这把必须使用是: {selected_guns}的枪")
