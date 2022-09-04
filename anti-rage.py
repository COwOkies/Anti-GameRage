import keyboard
import time
import pyperclip

#you can add/edit you own words here
badwords=["pos","shit","fucking","dumb","idiot","cunt","bastard","scumbag","bitch","hate","dick","arsehole","asshole"]
goodwords=["friend","cake","splendid","cool","smart","silly","baka","schoolbag","cat","like","pp","unicorn","poney"]

#USER CHANGES HERE
key = 't' #change the key. ctrl+"key" to launch.
autosend = True # True or False, autosend enable or not

#program 
while True:
    if keyboard.is_pressed("ctrl+"+key):
            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('ctrl+x')
            time.sleep(0.3)
            if keyboard.is_pressed('ctrl') != True:
                text = pyperclip.paste()
                words = text.split()
                
                for i in range(len(words)):
                    for j in range(len(badwords)):
                        if words[i] == badwords[j] or words[i] == badwords[j]+"s":
                            if words[i] == badwords[j]+"s":
                                words[i] = goodwords[j]+"s"
                            else:
                                words[i] = goodwords[j]

                   
                new_text = ' '.join(words)
                print(f"{text} --> {new_text}")
                keyboard.write(new_text)
                if autosend:
                    keyboard.press_and_release('return')
                
