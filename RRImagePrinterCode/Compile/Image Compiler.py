#V: Laku_2023_05_08
try:
    from pyautogui import *
    from PIL import Image
    import math
    import os
    import time
    import sys
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    print('module missing')
    input()
    exit()


Path = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/strings")

Ppath = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/CustomColors")
RecRoomColors= [
    

]


RecRoomMarks =[
        '~',
'`',
'!',
'@',
'#',
'$',
'%',
'^',
'&',
'*',
'(',
')',
'_',
'-',
'+',
'=',
'{',
'[',
'}',
']',
'|',
'„',
':',
';',
'"',
"'",
'<',
',',
'>',
'.',
'?',
'/',
'†',
'‡',
'‹',
'•',
'™',
'›',
'¡',
'¤',
'¦',
'«',
'°',
'±',
'²',
'³',
'»',
'¹',
'¼',
'½',
'¾',
'¿',
'¨',
'¬',
'¯',
'·',
'¸',
'º',
'¢',
'£',
'ò',
'ó',
'€',
'´',
'§',
'©',
'¶',
'ä',
'ö',
'w',
'W',
'q',
'Q',
'Z',
'X',
'x',
'Ä',
'Ö',
'å',
'Å',
'À',
'Á',
'Â',
'Ã',
'Æ',
'Ç',
'È',
'É',
'Ê',
'Ë',
'Ì',
'Í',
'Î',
'Ï',
'Ð',
'Ñ',
'Ò',
'Ó',
'Ô',
'Õ',
'×',
'Ø',
'Ù',
'Ú',
'Û',
'Ü',
'Ý',
'Þ',
'ß',
'à',
'á',
'â',
'ã',
'æ',
'ç',
'è',
'é',
'ê',
'ë',
'ì',
'í',
'î',
'ï',
'ð',
'ñ',
'ô',
'õ',
'÷',
'ø',
'ù',
'ú',
'û',
'ü',
'ý',
'þ',
'ÿ',
'…',
'Œ',
'œ',
'Ŋ',
'ŋ',
'Ώ',
'A',
'I',
'U',
'E',
'Λ',
'Θ',
'Ξ',
'Π',
'Φ',
'ή'

    ]



#~`!@#$%^&*()_-+={[}]|„:;"'<,>.?/†‡‹•™›¡¤¦«°±²³»¹¼½¾¿¨¬¯·¸º¢£òó€´§©¶äöwWqQZXxÄÖåÅÀÁÂÃÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕ×ØÙÚÛÜÝÞßàáâãæçèéêëìíîïðñôõ÷øùúûüýþÿ…ŒœŊŋΏAIUEΛΘΞΠΦήz
def main():
    from tkinter import filedialog
    imgfile =filedialog.askopenfilename()
    print("Choose image")
    fileName =  imgfile
    
    try:
        img = Image.open(fileName)
    except:
        print('not found')
        input()
        exit()
    print("Image obtained.")
    (siz1,siz2)= img.size
    newWidth = siz1
    newHeight = siz2
    img = img.convert("RGBA")
    img = img.resize((newWidth,newHeight),Image.Resampling.BICUBIC)
    print("Image resolution set to " + str(img.size[0]) + " by " + str(img.size[1]))
    input("Press enter to compile strings")
    print("Compiling strings...")
    before = milliseconds = float(time.time())
    (compiledString,img) = singleCompile(img)
    after = milliseconds = float(time.time())
    amountTime = round(after - before,2)
    print("Compiled 1 " + str(len(compiledString)) + " length string in " + str(amountTime) + " seconds.")
    print("Optimizing string...")
    before = len(compiledString)
    compiledString = optimizeString(compiledString)
    after = len(compiledString)
    print("Optimized string from length " + str(before) + " to length " + str(after) + ".")
    maxStringLength = 280
    strings = splitString(compiledString,maxStringLength)
    #prints change in string size
    print("Split compiled string into one list of length " + str(len(strings)) + ".")
    img.save(os.path.join(os.getcwd(),'result.png'))
    print("Saved resulting RR color image result.png")
    outputFile = open(Path,"w")
    for strA in strings:
        outputFile.write(strA + "\n")
    outputFile.close()
    print('Lists needed: '+str((round(len(strings)/65)*10)/10))
    print('Import time estimate: '+ str(round((4*len(strings))/60)) + ' Minutes' )
    input()
           
        
    
def displayResolution(image):
    [width,height] = image.size
    print('Width: ' + str(width) + '\nHeight: ' + str(height))

def singleCompile(image):
    [width,height] = image.size
    compiledString = ""
    symbolForColor = ''
    for x in range(0,int(width)):
        for y in range(0, height):
            (imgR,imgG,imgB,imgA) = image.getpixel((x,y))
            leastDeviation = 100000
            if(imgA == 0):
                value = (0,0,0,0)
                image.putpixel((x,y,), value)
                compiledString += "z"
            else:
                for i in range(0, len(RecRoomColors)):
                    (recR,recG,recB,symbol) = RecRoomColors[i]
                    deviation = math.sqrt(pow((imgR-recR),2)+pow((imgG-recG),2)+pow((imgB-recB),2))
                    if deviation < leastDeviation:
                        leastDeviation = deviation
                        symbolForColor = symbol
                        rForPixel = recR
                        gForPixel = recG
                        bForPixel = recB
                value = (rForPixel,gForPixel,bForPixel)
                compiledString += symbolForColor
                image.putpixel((x,y,), value)

    return (compiledString,image)

def splitString(string,maxLength):
    count = 0
    listString = []
    tempString = ""
    for i in string:
        count += 1
        tempString += i
        if count%maxLength == 0:
            listString.append(tempString)
            tempString = ''
    listString.append(tempString)
    return listString

def optimizeString(string):
    optimizedString = ""
    stringSegment = ""
    count = 0
    i = 0
    bool = True
    while i < len(string):
        symbol = string[i]
        if i+1+count > len(string)-1:
                bool = False  
        while(bool and symbol == string[i + 1 + count]):
            count += 1
            if i+1+count > len(string)-1:
                bool = False
                break
        if count+1 > 2:
            optimizedString += str(count+1) + symbol
        else:
            optimizedString += symbol*(count+1)
        i+= count
        count = 0
        i+=1
    return(optimizedString)

if __name__ == '__main__':
    try:
        open(Ppath)
    except:
        print('No Colorfile found')
        input()
        exit()
    with open(Ppath) as tiedosto:
        kohta=0
        for i in tiedosto:
            split= i.split('.')
            tup=split[0]
            color=eval(tup)
            try:
                RecRoomColors.append((int(color[0]),int(color[1]),int(color[2]),RecRoomMarks[kohta]))
            except:
                pass
            kohta+=1
    
    main()

