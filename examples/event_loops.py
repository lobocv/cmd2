#!/usr/bin/env python
# coding=utf-8
"""A sample application for integrating cmd2 with external event loops.

This is an example of how to use cmd2 in a way so that cmd2 doesn't own the inner event loop of your application.

This opens up the possibility of registering cmd2 input with event loops, like asyncio, without occupying the main loop.
"""
import cmd2


class Cmd2EventBased(cmd2.Cmd):
    def __init__(self):
        cmd2.Cmd.__init__(self)

    # ... your class code here ...


if __name__ == '__main__':
    app = Cmd2EventBased()
    app.preloop()

    # Do this within whatever event loop mechanism you wish to run a single command
    app.onecmd_plus_hooks("help history")

    app.postloop()
