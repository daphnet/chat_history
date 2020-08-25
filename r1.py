# 75 [程式練習] 對話紀錄1 - 格式改寫
# 讀取input.txt，更改格式後，輸出成output.txt



# read file
def read_file(file_name):
    lines = []
    # encoding='utf-8-sig'，可以把檔案頭的編碼符號去除
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        for line in f:
            #name, words = line.strip().split(':')
            lines.append (line.strip())
    return lines

# 改格式
# 原想法
# 1. for loop
# 2. 遇到人名，尾端加': '，併下一行
# 3. 沒有人名在前句，延用原人名，尾端加': '，併下一行
# 3.寫入清單
# 老師方法
# 1. for loop
# 2. 遇到人名，把人名標籤存起來，該行跳過不寫入清單
# 3. 真正的對話記錄前加上 '人名'，': '
# 4. 寫入清單
# 5. 處理下一行
# 小問題，如果對話紀錄第一行不是人名怎麼辦？
# 原程式會當掉，因為變數person還沒有宣告
# 解決方法：在for loop外先宣告person並給值，
# 如果person不等於我預先設定的值，
# 才做後面的 清單.append
# Python有針對此情況設計出'None'這個預設值
# 可在for loop前先宣告person = None，有宣告變數但值為「無」
# 似其他程語言的null

def convert(lines):
    new = []
    # person = '123'
    person = None
    # 把input的內容一行一行拿出來，加進lines清單
    for line in lines:
        # print(line)
        if line == 'Allen':
            person = 'Allen'
            continue # 跳到下一迴
        elif line == 'Tom':
            person = 'Tom'
            continue # 跳到下一迴
        # if person != '123':
        if person: # 可理解為如果person有值才做下面的動作
            new.append(person + ': ' + line)
    # print(new)
    return new

def write_file(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    # print(lines)
    # convert(lines)
    # 把lines = read_file('input.txt')的lines
    # 傳到convert(lines)的lines參數
    lines = convert(lines)
    write_file('output.txt', lines)

main()

