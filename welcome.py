def welcome():
    """
    Welcome function that will run first when the program is started,
    asking for the users to input Y or N whether they want
    to play the game or not.
    """
    print("""
      __        __   __         ___    ___  __
|  | /  \ |    /  ` /  \  |\/| |__      |  /  \                       |/|
|/\| \__/ |___ \__, \__/  |  | |___     |  \__/                       | |
                                                                      |/|
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗      | |
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║      |/|
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║     (___)
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║     (___)
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║     (___)
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ,(/   \),
 __              ___                                              ('/     \')
/ _`  /\   |\/| |__                                               |/|     |/|
\__> /~~\  |  | |___                                              (-\     /-)
                                                                   \-\___/-/
                                                                    '-----'
*****************************************************************************
""")
    # Ask the user if want to play or not and take in the input from the user
    playing = input("Would you like to play the game? [Y/N]: ").lower()
    print(playing)

    # If else statement that will run or quit the game.
    # Or restart the welcome message based on the users input.
    if playing == "y":
        pass

    elif playing == "n":
        quit()

    else:
        welcome()
