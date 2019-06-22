#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  openbox-pipemenu-steam.py
#
#  Copyright 2017 kirbylife <https://github.com/ImNotRoot>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os

try:
    from commands import getoutput, getstatusoutput
except:
    from subprocess import getoutput, getstatusoutput

STEAM_URL = os.environ['HOME'] + "/.steam/steam/steamapps"


def set_item(name, appid=None):
    if appid:
        print("<item label='" + name +
              "'><action name='Execute'><command>steam steam://rungameid/" +
              appid + "</command></action></item>")
    else:
        print("<item label='" + name + "'></item>")


def main(args):
    games = []

    ### Header ###
    print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    print("<openbox_pipe_menu>")
    ###        ###

    if getstatusoutput("cd " + STEAM_URL)[0] == 1:
        set_item("Steam not installed")
    else:
        games = getoutput("ls " + STEAM_URL + " | grep acf").split("\n")
        if not games:
            set_item("0 games installed")
        else:
            for c in games:
                appid = ""
                name = ""
                manifest = open(STEAM_URL + "/" + c, "r")
                data = manifest.read().split("\n")
                manifest.close()
                for f in data:
                    if '"appid"' in f:
                        appid = f.split('"')[3]
                    elif '"name"' in f:
                        name = f.split('"')[3]
                set_item(name, appid)

    ### Footer ###
    print("</openbox_pipe_menu>")
    ###        ###
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
