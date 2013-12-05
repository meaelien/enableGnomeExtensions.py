enableGnomeExtensions.py
========================

Python script used to enable gnome extensions at startup

Sometimes in some versions of Gnome Shell, extensions are disabled after reboot. It's very boring and I could not wait for the bug fix so I implemented this script that enable all extensions.

You just have to add it to your startup applications and everything should be ok.

Don't forget to make it executable with `chmod +x enableGnomeExtensions.py` and then `gnome-session-properties` to manage startup applications.