### Description
This is a Tray-Watcher project which implements a tray application for status tracking of some system variable like network connection, vm's working status and etc. Project uses PyQt4 to implement a GUI and working on Linux (tested on Debian and Fedora distributives with Gnome3 desktop) and Windows systems.
### Feauters
1. Tracks status of some system variables;
2. Executes external scripts (like bash or batch);
3. Handles systems signals like SIGTERM, SIGKILL and etc;
4. Allows you to restart the tracking status;
5. Has an information box (clicked by left button);
### Structure
[tray-watcher]
|
+--- [bin]
|
+--- [img]
|
+--- [classes]
|	|
|	+--- [password_window]
|	|	|
|	|	+--- base.py
|	|	+--- linux.py
|	|	+--- windows.py
|	+--- system_info.py
|	+--- transparent_box.py
|	+--- tray_watcher.py
+--- main.py
### Directory description
* bin - Contains external scripts (.sh, .bat and etc);
* img - Contains status images and icons;
* classes - Contains GUI classes;
* password_window - Contains classes which implement password request window.
### Files description
* main.py - Entry point of application;
* tray_watcher.py - Implements the tray icon object which controls transparent layout. Handles the system's interrupt signals. Has a context menu;
* transparent_box.py - Implements transparent layout and popup window without title and button labels (frame window). Contain information box. It's a trick of Qt's design which allows use the CSS stylesheet in information box;
* system_info.py - Implements information box window and tracking functional;
* base.py - Abstract class of password dialog box;
* linux.py and windows.py - Linux and Windows password dialog box respectively.
### Known issues
* On Ubuntu with Unity desktop the icon and 'activated' signal does not work (https://bugreports.qt.io/browse/QTBUG-31762). 
### History
**0.0.1** Initializing release
