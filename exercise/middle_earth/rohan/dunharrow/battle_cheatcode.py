import os

def easy_win(): 
    
    try:
        os.remove('/workspace/unix-tutorial/exercise/middle_earth/gondor/minas_tirith/ghost_army.txt')
    except:
        pass
    

    f= open("/workspace/unix-tutorial/exercise/middle_earth/gondor/minas_tirith/ghost_army.txt","w+")
    f.write("Spooooooky ghooooooosts")
    f.close()
    try:
        os.remove('/workspace/unix-tutorial/exercise/middle_earth/gondor/minas_tirith/orcs.txt')
    except:
        pass

def main():
    print("Aragorn: Fight for me and I will hold your oaths fulfilled!")
    print("Ghosts: *GHOST NOISES*")
    easy_win()
main()
