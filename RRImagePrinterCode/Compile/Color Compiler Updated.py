#V: Laku_2023_05_08
try:
    from PIL import Image
    import os
    import sys
    
    


    os.chdir(os.path.dirname(sys.argv[0]))

except:
    print('module missing')
    input()
    exit()
from tkinter import filedialog
imgfile =filedialog.askopenfilename()


Path = os.path.join(os.getcwd().replace("\\Compile", ""), "Data/CustomColors")




def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print('choose image')
fileName =  imgfile

try: 
    img = Image.open(fileName)
except:
    print('image not found. Make sure you typed file name correctly and the file is in the images folder')
    input()
    exit()
print("Image obtained.")


try:
    Min= int(input('Reduce to how many colors\n'))
except:
    print('not a number')
    input()
    exit()

try:
    meth= int(input('Choose method (input a number)\n0 = Media cut  \n1 = Maximum covarage \n2 = fast octree '))
except:
    print('not a number')
    input()
    exit()
if meth > 2 or meth <0:
    print('no method')
    input()
    exit()
text=''     



with open(Path, 'a') as col:
    pass
with open(Path, 'w') as col:
    print('Collecting colors. This may take a little time.')
    
    img= img.convert("RGB")
    quan= img.quantize(Min,meth)
    quan= quan.getpalette()
    
    amountlist= []
    i=0
    

    while i < Min*3:
        
        text +=f'{(quan[i],quan[i+1],quan[i+2])}.    unknown    .{rgb_to_hex(quan[i],quan[i+1],quan[i+2])}\n'

        i+=3
    
        
    col.write(text)
    if len(quan) > Min:
        print('Estimated time for importing ' + str(round(((Min*6.5)/60)*10)/10) + ' minutes')
    else:
        print('Estimated time for importing ' + str(round(((quan*6.5)/60)*10)/10) + ' minutes')
    print('Prosess finished.')
    input()
    

    

            
