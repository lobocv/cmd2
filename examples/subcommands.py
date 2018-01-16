"""
Create a CLI with a nested command structure as follows. The commands subcommand_* navigate the CLI to the scope
of the subcommand. Nesting of the subcommands is done with the register_subcommand() function.

      (Root)                        (Level 1)              (Level 2)

        A0
        |
        |-------subcommand_a--------->  A0_B0 --------subcommand_ab------> A0_B0_C0
        |
        |-------subcommand_b--------->  A0_B1



"""

from __future__ import print_function
import cmd2


class A0(cmd2.Cmd):
    """Root command class. Call register_subcommand() of this class to add subcommand(s). """
    def do_rootcommand(self, line):
        print("You called rootcommand!")
        pass

    def help_rootcommand(self):
        print('This is the help for rootcommand')


class A0_B0(cmd2.Cmd):
    """To be used as a second level command class. """
    def do_command_0(self, line):
        print("You called a command in subcommand_a with '%s'" % line)

    def help_command_0(self):
        print("This is a second level subcommand (subcommand_a). Options are qwe, asd, zxc")

    def complete_command_0(self, text, line, begidx, endidx):
        return [s for s in ['qwe', 'asd', 'zxc'] if s.startswith(text)]


class A0_B1(cmd2.Cmd):
    """To be used as a second level command class. """
    def do_command_1(self, line):
        print("You called a command in subcommand_b with '%s'" % line)

    def help_command_1(self):
        print("This is a second level subcommand (subcommand_b)`. Options are qwe, asd, zxc")

    def complete_command_1(self, text, line, begidx, endidx):
        return [s for s in ['qwe', 'asd', 'zxc'] if s.startswith(text)]


class A0_B0_C0(cmd2.Cmd):
    """To be used as a third level command class. """
    def do_command_0(self, line):
        print("You called a command in subcommand_ab with '%s'" % line)

    def help_command_0(self):
        print("This is a third level subcommand (subcommand_ab). Options are qwe, asd, zxc")

    def complete_command_0(self, text, line, begidx, endidx):
        return [s for s in ['qwe', 'asd', 'zxc'] if s.startswith(text)]



if __name__ == '__main__':
    # Nested for visual purposes
    root = A0()
    if 1:

        a0b0 = A0_B0()
        if 1:
            a0b0c0 = A0_B0_C0()

        a0b1 = A0_B1()


    root.register_subcommand(subcommand_a=a0b0, subcommand_b=a0b1)
    a0b0.register_subcommand(subcommand_ab=a0b0c0)

    root.cmdloop()

