import os
import sys
from tkinter.messagebox import showinfo

def Mise_a_jour():
    showinfo("Info maj","La mise à jour commence!")
    os.system('git pull')
    os.system('pyinstaller --onefile main.py')
    os.system('cp -f dist/main main')
    os.system('rm -r dist')
    os.system('rm -r build')
    os.system('rm main.spec')
    showinfo("Info maj","La mise à jour est terminée!")

def CreateApp():
    chemin = os.getcwd()
    print("choisir un prénom au tamagotchi:")
    tamaNom = input()
    f = open("/usr/share/applications/assistantsimpy.desktop",'w')
    f.write("[Desktop Entry]\n")
    f.write("Name= Mon Assistant "+tamaNom+"\n")
    f.write("Exec="+chemin+'/main\n')
    f.write("Type=Application\n")
    f.write("Icon="+chemin+'/Icon/Simpy.png\n')
    f.close()

if __name__ == '__main__':
    argv = sys.argv
    if not(len(argv) == 1) and argv[1] == 'app':
        CreateApp()
    else:
        Mise_a_jour()
