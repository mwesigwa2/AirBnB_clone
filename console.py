#!/usr/bin/python3
"""
This module gives the definition of the HBNBCommand class, the
command interpreter for the AirBnB clone project.
"""

import cmd

from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """defines the HBNB command interpreter.
    Attributes:
    prompt (str): the command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        command to exit the program
        """
        return True

    def do_emptyline(self, line):
        """
        Do nothing upon receiving an empty line
        """
        pass

    def do_EOF(self, line):
        """
        EOF signal to exit program
        """
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
