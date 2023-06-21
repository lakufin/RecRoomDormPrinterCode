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
    print('one  or more modules missing')
    input()
    exit()
Path = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/strings")
RecRoomColors =[
    (228, 80, 80,'~'),#Main colors start here
    (211, 23, 24,'`'),#1
    (118, 8, 8,'!'),#2
    (124, 47, 47,'@'),#3
    (240, 127, 790,'#'),#4
    (245, 92, 27,'$'),#5
    (193, 55, 9,'%'),#6
    (126, 66, 46,'^'),#7
    (247, 215, 105,'&'),#8
    (245, 197, 32,'*'),#9
    (180, 99, 0,'('),#10
    (130, 97, 56,')'),#11
    (137, 177, 81,'_'),#12
    (105, 163, 24,'-'),#13
    (47, 77, 8,'+'),#14
    (66, 82, 43,'='),#15
    (103, 189, 122,'{'),#16
    (16, 101, 34,'['),#17
    (6, 59, 17,'}'),#18
    (50, 76, 56,']'),#19
    (102, 218, 205,'|'),#20
    (1, 155, 137,'„'),#21
    (0, 80, 72,':'),#22
    (51, 86, 83,';'),#23
    (101, 199, 236,'"'),#24
    (1, 171, 233,"'"),#25
    (6, 87, 117,'<'),#26
    (50, 91, 106,','),#27
    (101, 160, 242,'>'),#28
    (24, 107, 221,'.'),#29
    (5, 57, 128,'?'),#30
    (49, 79, 121,'/'),#31
    (165, 133, 242,'†'),#32
    (80, 24, 221,'‡'),#33
    (47, 18, 120,'‹'),#34
    (86, 72, 120,'•'),#35
    (225, 148, 241,'™'),#36
    (120, 66, 131,'›'),#37
    (65, 24, 73,'¡'),#38
    (88, 61, 93,'¤'),#39
    (237, 120, 178,'¦'),#40
    (234, 46, 80,'«'),#41
    (130, 8, 64,'°'),#42
    (103, 56, 78,'±'),#43
    (125, 64, 25,'²'),#44
    (68, 40, 22,'³'),#45
    (61, 29, 13,'»'),#46
    (37, 16, 7,'¹'),#47
    (197, 132, 92,'¼'),#48
    (143, 99, 71,'½'),#49
    (90, 63, 49,'¾'),#50
    (38, 28, 22,'¿'),#51
    (246, 238, 233,'¨'),#52
    (191, 188, 186,'¬'),#53
    (152, 149, 147,'¯'),#54
    (124, 120, 119,'·'),#55
    (98, 100, 102,'¸'),#56
    (73, 74, 77,'º'),#57
    (44, 46, 50,'¢'),#58
    (25, 23, 23,'£'),#59
    (255, 181, 136,'ò'),#60
    (255,255,255,'ó'),#61
    (1, 1, 1,'€'),
    (255,255,255,'´'),
    (255, 255, 255,'§'), #main colors stop here
     (83, 12, 91, '©'),
    (197, 85, 65, '¶'),
    (250, 184, 56, 'ä'),
    (152, 21, 18, 'ö'),
    (70, 135, 47, 'w'),
    (243, 214, 128, 'W'),  
    (236, 162, 28, 'q'),
    (168, 80, 0, 'Q'),
    (108, 62, 32, 'Z'),
    (119, 162, 86, 'X'),
    (95, 150, 17, 'x'),
    (41, 69, 10, 'Ä'),
    (74, 85, 46, 'Ö'),
    (122, 199, 149, 'å'),
    (17, 111, 44, 'Å'),
    (83, 12, 91, 'À'),
(197, 85, 65, 'Á'),
(250, 184, 56, 'Â'),
(152, 21, 18, 'Ã'),
(70, 135, 47, 'Æ'),
(243, 214, 128, 'Ç'),
(236, 162, 28, 'È'),
(168, 80, 0, 'É'),
(108, 62, 32, 'Ê'),
(119, 162, 86, 'Ë'),
(95, 150, 17, 'Ì'),
(41, 69, 10, 'Í'),
(74, 85, 46, 'Î'),
(122, 199, 149, 'Ï'),
(17, 111, 44, 'Ð'),
(145, 28, 65, 'Ñ'),
(207, 160, 16, 'Ò'),
(93, 42, 61, 'Ó'),
(11, 143, 114, 'Ô'),
(173, 14, 145, 'Õ'),
(202, 128, 164, '×'),
(186, 168, 12, 'Ø'),
(46, 117, 159, 'Ù'),
(75, 148, 129, 'Ú'),
(57, 17, 79, 'Û'),
(132, 186, 214, 'Ü'),
(8, 87, 182, 'Ý'),
(209, 186, 238, 'Þ'),
(95, 68, 121, 'ß'),
(177, 108, 160, 'à'),
(203, 230, 99, 'á'),
(120, 81, 164, 'â'),
(19, 55, 94, 'ã'),
(114, 194, 183, 'æ'),
(45, 101, 141, 'ç'),
(81, 35, 93, 'è'),
(18, 47, 16, 'é'),
(182, 206, 64, 'ê'),
(54, 36, 33, 'ë'),
(237, 237, 237, 'ì'),
(140, 139, 138, 'í'),
(117, 138, 117, 'î'),
(60, 128, 161, 'ï'),
(220, 179, 136, 'ð'),
(81, 85, 90, 'ñ'),
(213, 164, 187, 'ô'),
(204, 82, 72, 'õ'),
(186, 186, 186, '÷'),
(189, 222, 255, 'ø')
#(135, 68, 34, 'ù'),
#(176, 101, 41, 'ú'),
#(179, 193, 210, 'û'),
#(201, 98, 105, 'ü'),
#(155, 88, 84, 'ý'),
#(102, 118, 122, 'þ'),
#(193, 190, 203, 'ÿ'),
#(145, 175, 161, '…'),
#(75, 68, 80, 'Œ'),
#(100, 116, 120, 'œ')



]
#(181, 230, 29, 'Ŋ'),
#(56, 153, 231, 'ŋ'),
#(17, 52, 172, 'Ώ'),
#(0, 255, 255, 'A'),
#(255, 0, 0, 'I'),
#(255, 255, 0, 'U'),
#(128, 0, 128, 'E'),
#(0, 128, 0, 'Λ'),
#(0, 0, 255, 'Θ'),
#(128, 128, 128, 'Ξ'),


def main():
    from tkinter import filedialog
    imgfile =filedialog.askopenfilename()
    print("choose image")
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
    print("Image resolution is " + str(img.size[0]) + " by " + str(img.size[1]))
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
    main()
    
