# 76 [程式練習] 對話紀錄2 - part 1
# 讀取line對話紀錄input.txt，更改格式後，輸出成output.txt

# 77 清單的切割，有三種
# n = [2, 6, 6, 8, 4]
#    n[0] n[1] n[2] n[3] n[4]
# 1. 前3個，n[:3] -> 表示0:3，0到3，開始值:結束值，
#    開始值從0開始，0可以省略，開始值有包含，結束值不包含，
#    -> n[0], n[1], n[2] -> [2, 6, 6]
# 2. 中間，n[2:4]，-> 開始值有包含，結束值不包含，
#    -> n[2], n[3] -> [6, 8]
# 3. 結尾，n[-2:]，負號表示從結尾往回拿倒數兩個，
#    -> n[3], n[4] -> [8, 4]

# 78 [程式練習] 對話紀錄2 - part 2

# read file
def read_file(file_name):
    lines = []
    # encoding='utf-8-sig'，可以把檔案頭的編碼符號去除
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append (line.strip())
    return lines

# 統計每個人講了幾個字，傳了幾張貼圖跟圖片

def convert(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_img_count = 0
    viki_img_count = 0

    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count +=1
            elif s[2] == '圖片':
                allen_img_count +=1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count +=1
            elif s[2] == '圖片':
                viki_img_count +=1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)

    print('Allen said', allen_word_count, 'words, sent', allen_sticker_count, 'stickers,', allen_img_count, 'images')
    print('Viki said', viki_word_count, 'words, sent', viki_sticker_count, 'stickers,', viki_img_count, 'images')


# 寫檔案
def write_file(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()




