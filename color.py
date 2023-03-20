import os
import time


os.system('color') #windows only

time.sleep(0.1)
def CTXT(text):
    text_count = 0
    text_count_end = 0
    text_count_HEX = 0
    text_count_HEX_end = 0
    while text_count != -1:
        text_count = text.find('$',text_count)
        text_count_end = text.find('>',text_count) + 1
        text_esc = text[text_count:text_count_end]
        text_esc_old = text_esc
        if "#" in text_esc :
            while text_count_HEX != -1:
                text_count_HEX = text_esc.find('#',text_count_HEX)
                text_count_HEX += 1
                text_count_HEX_end = text_count_HEX + 6
                text_HEX = text_esc[text_count_HEX:text_count_HEX_end]
                 
                text_esc = text_esc[:text_count_HEX - 1] + str(tuple(int(text_HEX[i:i+2], 16) for i in (0, 2, 4))).translate(str.maketrans({ ',':':' ,  '(':'',  ')':'' })) + text_esc[text_count_HEX_end:]
                
                text_count_HEX = text_esc.find('#',text_count_HEX)
        text = text.replace(text_esc_old,text_esc.translate(str.maketrans({'$':''    ,   'f':'\033[38;2;'  ,  'b':';48;2;'  ,  ':':';'  ,  '>':'m'  , ' ':''})))
   
        
    else:
        return text + "\033[00m"

#demo

print(CTXT("$f 0 : 255 : 0 >Hello world!"))
print(CTXT("$f#00ff00>green text!!"))
print(CTXT("$f#000000 b#ffffff>white-back,black-text!"))
font_color = 123456
back_color =098765
print(CTXT(f"$f#{font_color}b#{back_color}>yesyesyeees"))
