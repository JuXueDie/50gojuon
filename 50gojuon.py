import csv
import random

HIRAGANA_FILE = "hiragana.csv"
KATAKANA_FILE = "katakana.csv"

global score
score = 0
global giveup
giveup = False

def printcsv(user_input):
    # input = 3
    if user_input == '5':
        csvfile = HIRAGANA_FILE
    elif user_input == '6':
        csvfile = KATAKANA_FILE
    with open(csvfile, newline='', encoding='utf_8') as csvfile:

        # 直接讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # 以迴圈輸出指定欄位
        for row in rows:
            print(row['let'], row['pron'])

def show_option():
    user_input = input("""[1]平假名無限挑戰/endless hiragana  [2]片假名無限挑戰/endless katakana
[3]平假名/hiragana                  [4]片假名/katakana
[5]印製平假名表/print hiragana table[6]印製片假名表/print katakana table
[Q/q]離開/quit
>>> """)
    return user_input


def endless_answer_pron(user_input):
    global score
    global giveup
    key = str(random.randint(1, 46))
    if user_input == '1':
        csvfile = HIRAGANA_FILE
    elif user_input == '2':
        csvfile = KATAKANA_FILE
    with open(csvfile, newline='', encoding='utf_8') as csvfile:
        rows = csv.DictReader(csvfile)
        i = 0
        for row in rows:
            # print(row)
            i += 1
            while str(i) == key:
                ques = row['let']
                user_ans = input(ques + ' ')
                if user_ans == row['pron']:
                    print('Correct')
                    score += 1
                    break
                elif user_ans == 'giveup':
                    print('Your score is {}'.format(score))
                    giveup = True
                    break
                else:
                    print('Failed')
        while giveup == False:
            endless_answer_pron(user_input)
        # print(key)
    # user_ans = input()

def answer_pron(user_input):
    global score
    if user_input == '3':
        csvfile = HIRAGANA_FILE
    elif user_input == '4':
        csvfile = KATAKANA_FILE
    with open(csvfile, newline='', encoding='utf_8') as csvfile:
        rows = csv.reader(csvfile)
        # 先創空字典再放進去
        csv_dict = dict()
        for row in rows:
            csv_dict[row[0]] = row[1]
    # print(csv_dict)

    let_list = list(csv_dict.keys())
    pron_list = list(csv_dict.values())

    # 將列表打亂後照新順序一一輸出
    num_list = list(range(1, len(csv_dict)))
    random.shuffle(num_list)
    # print(num_list)

    error_list = list()

    for i in num_list:
        print(let_list[i])
        user_ans = input()
        if user_ans == pron_list[i]:
            print('Correct')
            score += 1
        elif user_ans == 'giveup':
            break
        else:
            print('Failed, the ans is {}'.format(pron_list[i]))
            error_list.append(let_list[i])
            
    if len(error_list) == 0:
        print('Correct rate is {}/46'.format(score))
    else:
        print('Correct rate is {}/46'.format(score))
        print('Please remember:\n{}'.format(error_list))



def main():
    user_input = show_option()
    if user_input == '1' or user_input == '2':
        endless_answer_pron(user_input)
    elif user_input == '3' or user_input == '4':
        answer_pron(user_input)
    elif user_input == '5' or user_input == '6':
        printcsv(user_input)
    elif user_input == 'Q' or user_input == 'q':
        print('See you next time')
    else:
        print('Stop being stupid')

if __name__ == '__main__':
    main()