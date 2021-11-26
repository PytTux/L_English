import random

dosya = open("words","r")
kelimeler = dosya.readlines()
dosya.close()


def ask_q():
    kelime_say = random.randint(0,len(kelimeler)-1)
    print(kelimeler)
    kelime = kelimeler[kelime_say]
    kelime_l = kelime.split(":")
    tr     = kelime_l[0]
    eng    = kelime_l[1]
    true  = int(kelime_l[2])
    false = int(kelime_l[3])
    eng_ans = input(tr+" ingilizce karşılığı nedir ? \n : ")

    if eng_ans == "" or eng_ans == " ":
        return False
    elif eng_ans == eng:
        true += 1
        sonuc = True
    else:
        false += 1
        sonuc = False
    print(true,false)
    print(str(tr)+":"+str(eng)+":"+str(true)+":"+str(false))
    add_word(tr,eng,true,false)
    print(kelimeler)
    return sonuc

def reset_v():
    say = 0
    for kelime in kelimeler:
        kelime_l  = kelime.split(":")
        kelimeler[say] = str(kelime_l[0])+":"+str(kelime_l[1])+":"+"0"+":"+"0"
        say +=1
    print(kelimeler)

def add_word(tr,eng,true = 0, false = 0):
    for kelime in kelimeler:
        kelime_l = kelime.split(":")
        if str(kelime_l[0]) == tr or kelime_l[1] == eng :
            if tr == "" or eng == "" or tr == " " or eng == " ":
                break
    new_word = str(tr)+":"+str(eng)+":"+str(true)+":"+str(false)
    kelimeler.append(new_word)
    print(kelimeler)
    write_list()


def tr_eng_al():
    add_tr = input("türkçe kelimeyi giriniz :")
    add_eng = input("ingilizce kelimeyi giriniz :")
    return add_tr,add_eng

def write_list():
    for kelime in kelimeler:
        dosya = open("words","w")
        dosya.writelines(kelimeler)
        dosya.close()
        



