from gui_project1 import *


def main() -> None:
    """
    This function runs the GUI upon startup. It also
    gives the window a title "Voting Application" and
    sets the size of the GUI.
    """
    window = Tk()
    window.title("Voting Application")
    window.geometry("350x400")
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()