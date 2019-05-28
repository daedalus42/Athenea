# Athenea
Instructable DIY

-STL files: 
All the files needed are available at https://www.thingiverse.com/thing:3647372 for creative common use. If you want to replicate Athenea’s project we recommend you to print 4 pieces with the following parameters: 
Body_IR_holes: 3 layers shell, infill 20% and supports as needed.
Head_IR_holes: 1 single layer shell.
Eliptic_tube: 2-3 layers shell and infill between 20-30%.
Holder_DCmotor: same as Eliptic_tube.
We left all the versions of the 3D pieces we created to use our hardware as platform for future projects, see the following section, where we propose some implementations for future students.
-Python Code: 
All the code needed can be found at: https://github.com/daedalus42/Athenea
Install an OS on the Raspberry Pi microSD, available in the following link: https://www.raspberrypi.org/downloads/
You can work directly on RPi with screen and peripherals or SSH (https://www.raspberrypi.org/documentation/remote-access/ssh/)
Install:
Opencv
Google cloud vision and speech
RPi.GPIO
Picamera
Pygame
Numpy
Six.moves
Sys
Os
Re
Time
Install dependencies as needed while installing other libraries.
Copy the code from our gitHub: https://github.com/daedalus42/Athenea
Get credentials for Google Cloud at https://cloud.google.com/genomics/docs/how-tos/getting-started
Open the configuration file and set up Google Cloud JSON credentials location. In this file you can change pins assignments if needed.

-Hardware list: 
RaspberryPi 3 B+, MicroSD 32Gb, RPI NOIR Camera.
USB Microphone, USB Speaker.
Infrared sensor (QRD1114) - four.
RGB led 5050 strip.
DC Motor.
PSU 5V and 12V.
Motor Controller: L298N chip - four.
Resistors four 4,7kΩ & four 220Ω, cables, thermoplastic tubing, prototyping board.
Tools: soldering iron, solder, heater, cable cutter, hot glue gun, 3D printed pieces.

Assembly:
RPi Noir Camera connection to RPi on the camera socket.
Speaker connection via bluetooth.
Microphone connection via USB.
External power supply unit (PSU) (shown in fritzing as 4xAA batteries) connected to the components to 5V, 12V and common GND (ground) based on the needs of the components, GND has to be common to all components.
Install 2 motor controllers, to control up to 4 components, 3 will be used for led lightning control and one for the DC motor.
Both L298N gets as input 12V, 5V and GND.
First L298N RPi pins en(enable) on GPIO_16, in1 on GPIO_20, in2 on GPIO_21 a DC motor will be connected to out1 and out2.
First L298N RPi pins en(enable) on GPIO_25, in3 on GPIO_8, in4 on GPIO_7, green color on the led strip will be connected to out3 and out4.
Second L298N RPi pins en(enable) on GPIO_10, in1 on GPIO_9, in2 on GPIO_11, red color on the led strip will be connected to out1 and out2.
Second L298N RPi pins en(enable) on GPIO_17, in3 on GPIO_22, in4 on GPIO_27, blue color on the led strip will be connected to out3 and out4.
IR sensor QRD1114 needs a 4,7k Ω in pin 1 before being connected to 5V, pins 2 and 3 are connected to common GND and pin 3 requires 220Ω before being connected to 5V between the resistor and the 5V the sensor is connected to RPi GPIO_6, GPIO_13, GPIO_19, GPIO_26.

