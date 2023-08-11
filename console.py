#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(HBNH) "

    def do_quit(self, line):
        """
        doc
        """
        return True

    def do_emptyline(self, line):
        """
        doc
        """
        pass

    def do_EOF(self, line):
        """
        doc
        """
        pass

    def do_create(self, line):
        """
        doc
        """
if __name__ == "__main__":
    HBNBCommand().cmdloop()
