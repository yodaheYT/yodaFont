#                  _       ______          _   
#                 | |     |  ____|        | |  
#  _   _  ___   __| | __ _| |__ ___  _ __ | |_ 
# | | | |/ _ \ / _` |/ _` |  __/ _ \| '_ \| __|
# | |_| | (_) | (_| | (_| | | | (_) | | | | |_ 
#  \__, |\___/ \__,_|\__,_|_|  \___/|_| |_|\__|
#   __/ |                                      
#  |___/                                      
uppertable = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y",
    "Z", " "
]
lowertable = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
    "z", " "
]
numbertable = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "0"
]
specialtable = [
    " ", "_", "-", "!", ".",
    ",", ":", ";", "|", "/",
    "'", '"', "?", ">", "<",
    "~", "`", "#", "@", "$",
    "%", "^", "&", "*","(",
    ")", "[", "]", "{", "}"
]
def drawText(text, pos = (0,0), v2 = 1, display = None, fonttable = None):
    if display and fonttable:
        list = [char for char in text]
        for i in list:
            if i.isupper():
                for v in uppertable:
                    if i == v:
                        display.blit(fonttable, ((pos[0]+(v2*16)), pos[1]), (((uppertable.index(v)*16)),0,16,16))
                        v2+=1
            elif i.islower():
                for v in lowertable:
                    if i == v:
                        display.blit(fonttable, ((pos[0]+(v2*16)), pos[1]), (((lowertable.index(v)*16)),16,16,16))
                        v2+=1
            elif i.isnumeric():
                for v in numbertable:
                    if i == v:
                        display.blit(fonttable, ((pos[0]+(v2*16)), pos[1]), (((numbertable.index(v)*16)),32,16,16))
                        v2+=1
            else:
                for v in specialtable:
                    if i == v:
                        display.blit(fonttable, ((pos[0]+(v2*16)), pos[1]), (((specialtable.index(v)*16)),48,16,16))
                        v2+=1