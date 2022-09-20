import os
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

if __name__ == '__main__':
    Mise_a_jour()
