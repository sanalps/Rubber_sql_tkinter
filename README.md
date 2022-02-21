This desktop GUI is for managing an SQLite database for rubber compounds. This application can insert, delete, update and search SQLite database.

This app uses python inbuilt GUI Tkinter so this app does not require additional packageinstallation.

Sample sql database is also included in this repository

You need to change the database address to the correct address for the app to work (line131). You may have to use forward or backward slashes depending on whether your system is windows, mac, or linux.

con = sqlite3.connect('/home/rubber.db')