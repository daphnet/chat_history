# 79 [程式練習] 對話紀錄3 - 格式改寫

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    # 對話紀錄一開始的前5個字是時間，也就是s[0]的前5個字 -> s[0][:5]
    time = s[0][:5] # s[0][0, 1, 2, 3, 4]
    name = s[0][5:] # s[0][5, 6, 7, ...., end]
    print(time)
    print(name)