
from subprocess import call


def easy_win(): 
    
    f= open("/workspace/unix-tutorial/exercise/middle_earth/gondor/minas_tirith/ghost_army.txt","w+")
    f.write("Spooooooky ghooooooosts")
    f.close()

    call('rm /workspace/unix-tutorial/exercise/middle_earth/gondor/minas_tirith/orcs.txt')

def main():
    print("Aragorn: Fight for me and I will hold your oaths fulfilled!")
    print("Ghosts: *GHOST NOISES*")
    easy_win()
main()
