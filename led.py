

ledVerde = Motor()
ledAzul = Motor()
ledRojo = Motor()

ledRojo.pines(rIn1, rIn2, rEn)
ledVerde.pines(gIn2,gIn2, gEn)
ledAzul.pines(bIn2, bIn2, bEn)

ledAzul.init(bPWM)
ledVerde.init(gPWM)
ledRojo.init(rPWM)


def turnOff():
    ledAzul.stop()
    ledVerde.stop()
    ledRojo.stop()

#BRG
def turnOn(blue, red, green):
    turnOff()
    ledRojo.forward()
    ledAzul.forward()
    ledVerde.forward()

    if blue > 100:
        blue = 100
    if red > 100:
        red = 100
    if green > 100:
        green = 100
    ledAzul.start(blue)
    ledRojo.start(red)
    ledVerde.start(green)

def redOn(int=100):
    turnOn(1,int,1)

def redOff():
    ledRojo.stop()

def greenOn(int=100):
    turnOn(1,1,int)

def greenOff():
    ledVerde.stop()

def blueOn(int=100):
    turnOn(int,1,1)

def blueOff():
    ledAzul.stop()

#BR
def purpleOn(int1=50,int2=100):
    turnOn(int1,int2,1)

def purpleOff():
    ledAzul.stop()
    ledRojo.stop()

def whiteOn(in1=50,in2=100,in3=50):
    whiteOff()
    ledRojo.forward()
    ledAzul.forward()
    ledVerde.forward()
    turnOn(in1,in2,in3)

def whiteOff():
    ledAzul.stop()
    ledVerde.stop()
    ledRojo.stop()






