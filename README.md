 
# Directory-Monitoring-Watchdog
This poc is writed with ***Python*** to create a service to monitoring a state of a directory or folder, using ***Watchdog*** to handle these events when occur.

### Usage
* First install ***Watchdog***, to do this just use command `pip install watchdog`, if you don't have yet pip, install pip first.
* To run project, in folder of .py file run the command `python3 watchdog_event_handlers.py`, when project is running, just go to folder `monitoring-folder` in root project path and create, modifie and delete files to see working, application will log the events in the console.

### Acknowledgments
[Watchdog Documentation](https://pythonhosted.org/watchdog/)
