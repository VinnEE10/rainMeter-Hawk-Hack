#userinput of a diretory
#store that input and mod that directory
#create subfolder in the dir
#use a algo that finds the files and autosorts themD:

#Goal: Use a dictionary to asses files.

import os
import shutil

sourcepath = input("Enter a diretory to be sorted: ")
sourcefiles = os.listdir(sourcepath)

os.chdir(sourcepath)

if os.path.isdir('./images') == True:
    print ("ok")
else:
    os.mkdir('images')
    os.mkdir('vids')
    os.mkdir('exe')
    os.mkdir('zips')
    os.mkdir('audio')
    os.mkdir('text and word')
    os.mkdir('misc')

for file in sourcefiles:
    #images
    if file.endswith('.jpg'): #This catches the file you wcdant to sort
        shutil.move(os.path.join(sourcepath,file), os.path.join('./images',file))
    elif file.endswith('.png'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./images',file))
    elif file.endswith('.PNG'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./images',file))


    #vids
    elif file.endswith('.mov'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./vids',file))
    elif file.endswith('.mp4'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./vids',file))


    #text files
    elif file.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./text and word',file))
    elif file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./text and word',file))
    elif file.endswith('.docx'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./text and word',file))

    #others
    elif file.endswith('.iso'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./misc',file))
    elif file.endswith('.exe'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./exe',file))

    #zips rars
    elif file.endswith('.zip'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./zips',file))
    elif  file.endswith('.ZIP'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./zips',file))
    elif  file.endswith('.rar'):
        shutil.move(os.path.join(sourcepath,file), os.path.join('./zips',file))

