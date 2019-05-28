

class Motor:
    in1 = 0
    in2 = 0
    en = 0
    direccion = "f"  # f/b

    def __init__(self):
        pass

    def __del__(self):
        GPIO.cleanup()

    def pines(self, in1, in2, en):
        self.in1 = in1
        self.in2 = in2
        self.en = en

    def start(self, n=1):

        self.p.start(n)
    def init(self, n=1000):

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)

        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p = GPIO.PWM(self.en, n)

    def changeDirection(self):
        if self.direccion == "f":
            self.backward()

        elif self.direccion == "b":
            self.forward()

    def backward(self):
        self.direccion = "b"
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def forward(self):
        self.direccion = "f"
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def stop(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def low(self):
        self.p.ChangeDutyCycle(25)

    def medium(self):
        self.p.ChangeDutyCycle(50)

    def high(self):
        self.p.ChangeDutyCycle(100)

    def intensidad(self, n):
        self.p.ChangeDutyCycle(n)


