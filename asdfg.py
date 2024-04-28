from dddaccb import key_names
import play
from random import choice
color = "white"
def random_word():
    with open("words.txt", encoding="UTF-8") as file:
        return choice(file.read().split())
def frame():
    x, y = -146, 207
    for i in range(6):
        for j in range(5):
            play.new_box("white", x, y, 70, 80, "black", 2)
            x += 73
        x = -146
        y -= 83
index = 0
count = 0
gues = "01234"
hiden_word = random_word()
word_x, word_y = -146, 207
frame()
@play.repeat_forever
async def game():
    global word_x, word_y, count, index, gues
    for i in key_names:
        if play.key_is_pressed(i):
            # play.new_text(key_names[i]. upper(), word_x, word_y, None, 50)
            # if word_x < 146:
            #     word_x += 73
            # else:
            #     word_x= -146
            #     word_y -=83
            # await play.timer(0.1)
            if key_names[i]in hiden_word and hiden_word.find(key_names[i], index) == index:
                color = "green"
                gues = gues.replace(gues[index],(key_names[i]))
                print(gues)
            elif key_names[i] in hiden_word and hiden_word.find(key_names[i], index) != index:
                color = "orange"
            elif key_names[i] not in hiden_word:
                color = "grey"
            play.new_text(key_names[i]. upper(), word_x, word_y, None, 50)
            await play.timer(0.1)
            if word_x < 146:
                word_x += 73
                index += 1
            else:
                word_x = -146
                word_y -= 83
                index = 0
                if count == 5:
                    gues = "01234"
                else:
                    count = 0
    if gues == hiden_word:
        play.new_text("УГАДАЛ", 0, 0,None, 50)
        word_y = -300
        count = 5
play.start_program()
