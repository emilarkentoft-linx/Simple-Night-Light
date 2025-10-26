Python Packages Needed For Install:
Tkinter

____________________________________________________

How to build into an app:

Install pyinstaller and execute these commands in the dir:

pyinstaller --onefile nightlight.py

kdir -p ~/.local/share/applications
cd ~/.local/share/applications

nano nightlight.desktop

[Desktop Entry]
Name=Night Light
Comment=Adjust color temperature
Exec=/home/EmilArkentoft/Documents/Projects/Night_Light/dist/nightlight
Icon=preferences-desktop-color
Terminal=false
Type=Application
Categories=Utility;

chmod +x nightlight.desktop

update-desktop-database ~/.local/share/applications

____________________________________________________
