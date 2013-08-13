RoboPython
==========

An easy to use, Python/arduino based robotics kit


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Directions for use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The default port for the arduino to connect to is ./ttyACMO/ this will
be different on windows and mac and can be changed by editing the "ser" variable in the source files


Must use an arduino mega as show in the diagram, though planned updates are afoot for other models.

It will require motor drivers to provide enough current to actually run motors.

To import module put this at the top of your code: from RoboPython.robot import Robot

Requires Pyserial to work.

