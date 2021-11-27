import random

dosya = open("words","r")
kelimeler = dosya.readlines()
dosya.close()

def ask_q():
    try:
        dosya = open("words", "r")
        kelimeler = dosya.readlines()
    except  IOError:
        print("Error")
    finally:
        dosya.close()

    sayac = 0
    for kelime in kelimeler:
        sayac += 1
    rand_say = random.randint(0,sayac-1)
    asking_question = kelimeler[rand_say]
    asking_question = asking_question.split(":")
    true  = int(asking_question[2])
    false = int(asking_question[3])
    eng_taked = input(asking_question[0]+" ingilizce karşılığı nedir ? :")
    if eng_taked == asking_question[1]:
        true += 1
        add_word(str(asking_question[0]),str(asking_question[1]),rand_say,true,false)
    elif eng_taked != "" or eng_taked != " " and eng_taked != asking_question[1]:
        false +=1
        add_word(str(asking_question[0]),str(asking_question[1]),rand_say,true,false)
    else:
        print("boş geçmeyiniz")
    print(asking_question)




def add_word(tr, eng, line = None, true=0, false=0):
    try:
        dosya = open("words", "r+") # open type "a" can add lines to file without delete
        kelimeler = dosya.readlines()
        if true != 0 or false != 0:
            tr_eng_word = [tr,eng]
            print(kelimeler)
            kelimeler[line] = (str(tr_eng_word[0])+":"+str(tr_eng_word[1])+":"+str(true)+":"+str(false)+":"+"\n")
            print("say")
            dosya.seek(0)
            dosya.writelines(kelimeler)
        else:
            tr_eng_word = tr_eng_al()
            print(tr_eng_word)
            dosya.writelines(str(tr_eng_word[0])+":"+str(tr_eng_word[1])+":"+str(true)+":"+str(false)+":"+"\n")
    except  IOError:
        print("Error")
    finally:
        dosya.close()
        print("closed")

def reset_v():
    say = 0
    for kelime in kelimeler:
        kelime_l  = kelime.split(":")
        kelimeler[say] = str(kelime_l[0])+":"+str(kelime_l[1])+":"+"0"+":"+"0"
        say +=1
    print(kelimeler)

def tr_eng_al():
    add_tr = input("türkçe kelimeyi giriniz :")
    add_eng = input("ingilizce kelimeyi giriniz :")
    return [add_tr,add_eng]

def write_list():
    for kelime in kelimeler:
        dosya = open("words","w")
        dosya.writelines(kelimeler)
        dosya.close()