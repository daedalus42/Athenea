
from confing import *


face_cascade = cv2.CascadeClassifier(classifier)

irControl = Sensores()
motorControl= Motor()
emo = Emotion()
irControl.pines(WR,WL,ER,EL)
motorControl.pines(mIn1,mIn2,mEn)
motorControl.init(mPWM)
name = ""

class Happy:

    def interaccion(self):
        Owl_joke()
        time.sleep(3)

class Sad:

    def interaccion(self):
        tts.speak("....I feel sad would you mind touching my ears "+str(name)+", please?")

        for i in range(1):

            con = True
            con2 = True
            text= ""
            while con and con2 :
                con = not (irControl.detectaOrejaDerecho())
                con2 = not (irControl.detectaOrejaIzquierda())

            tts.speak("...Thank you "+str(name)+". I feel better now.")
            time.sleep(2)


class Angry:

    def interaccion(self):
        for i in range(3):
            con =True
            con2 =True

            while con and con2:
                con = not (irControl.detectaAlaDerecha())
                con2 = not (irControl.detectaAlaIzquierda())
            text = "Not that one! The other"
            print(text)
            tts.speak(text)

            time.sleep(1)


        print("Bye")



class Surprise():

    def interaccion(self):

        intensidad =50
        color = 1
        #adivinar sensor
        str ="...Surprise!. I’m Athenea an emocional owl that can do a lot of thing would you like to see it?"
        tts.speak(str)

        result = listenAnswer()
        if result == "yes":

            tts.speak("...Ok. Touch mi wings or ears")
            for i in range(2):
                con=True
                con2=True
                con3=True
                con4=True

                while (con and con2) and (con3 and con4):
                    con3 = not (irControl.detectaOrejaDerecho())
                    con4 = not (irControl.detectaOrejaIzquierda())
                    con = not (irControl.detectaAlaDerecha())
                    con2 = not (irControl.detectaAlaIzquierda())

                if not con:
                    text = "That’s my right wing."
                    tts.speak(text)


                if not con2:
                    text = " ..you touched my left wing,right?"
                    tts.speak(text)



                if not con3:
                    text=" .That’s my right ear."
                    tts.speak(text)


                if not con4:
                    text = "That’s my right ear."
                    tts.speak(text)


                    ledAzul.intensidad(intensidad-10)
                    ledRojo.intensidad(intensidad)
                time.sleep(3)
                if i != 1:
                    tts.speak("Again!")



            t =".... Now let’s do something creative. What’s your favourite color?" \
               " Touch my left wing to increase red, touch my  right wing to " \
               "increase blue, touch my  right ear to increase green and my " \
               " left ear to reset color if you want to start again"
            tts.speak(t)
            creaColor()
            t = "I’ll remember this color for you "+name+". Have a nice day."
            tts.speak(t)


def Capturar():
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='bgr')
            image = stream.array
            stream.seek(0)
            stream.truncate()
    return image

def enciendeLed(emocion):
    print(emocion)
    print("emocion")
    if emocion == 'Sad':
        interaccion = Sad()
        blueOn()
        interaccion.interaccion()
        blueOff()

    elif emocion == 'Happy':
        interaccion =Happy()
        greenOn()
        interaccion.interaccion()
        greenOff()

    elif emocion == 'Surprised' :
        interaccion = Surprise()
        purpleOn()
        interaccion.interaccion()
        purpleOff()

    else:
        interaccion = Angry()
        redOn()
        interaccion.interaccion()
        redOff()



def secuenciaDeColores():
    for i in range(2):
	    whiteOff()
	    ledVerde.start(1)
	    ledAzul.start(20)
	    ledRojo.start(100)
	    time.sleep(0.2)
	    whiteOff()
	    greenOn()
	    time.sleep(0.2)

	    redOn()
	    time.sleep(0.2)

	    blueOn()
	    time.sleep(0.2)

	    whiteOn()
	    time.sleep(0.2)

	    purpleOn()
	    time.sleep(0.2)


def creaColor():
        intensidad=[1,20,1]

        for i in range(100):
            con = True
            con2 = True
            con3 = True
            con4 = True
            while (con and con2) and (con3 and con4):
                con3 = not (irControl.detectaOrejaDerecho())
                con4 = not (irControl.detectaOrejaIzquierda())
                con = not (irControl.detectaAlaDerecha())
                con2 = not (irControl.detectaAlaIzquierda())

            if not con:
                #Azul
                if intensidad[0] <100:
                    intensidad[0]+=10
            if not con2:
                #Rojo
                if intensidad[1] <100:
                    intensidad[1]+=10

            if not con3:
                #Verde
                if intensidad[2] <100:
                    intensidad[2]+=20


            if not con4:
                intensidad = [1, 20, 1]

            whiteOn(intensidad[0],intensidad[1],intensidad[2])
            time.sleep(1)

        time.sleep(4)


print("iniciando...")

print("iniciando...")
whiteOn()
modelo = FacialRecognition()
print("preparandose...")
modelo.saveModel()
print("Buscando...")

cont=0

giro = "f"
estado = 0

try:
    while True:
        motorControl.stop()
        print("capturando")
        imagen = Capturar()
        cv2.imwrite('captura.png', imagen)
        if estado <= 1:
            motorControl.forward()
        else :
            motorControl.backward()


        estado+=1
        if estado == 4:
            estado = 0

        motorControl.start(15)

        size = 4
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
        result= modelo.detecionFacial(imagen)
        if result:
            motorControl.stop()
            prediccion=modelo.reconocimientoFacial(mini)
            personas = 0
            for i in range(len(prediccion)):
                if prediccion[1] > 100 and prediccion[1] < 130:
                    personas+=1

            name = modelo.getName(prediccion[0])
            texto = ""
            if personas >0:
                secuenciaDeColores()
                tts.speak("...Hi " + str(name))
                texto= "...I'm happy to see you again"
                tts.speak(texto)


            else :
                tts.speak("...Hello, I’m Athenea an emocional owl. I don’t recognize you. What’s your name?")
                time.sleep(5)
                tts.speak("...Hi"+str(name)+". Nice to meet you")
                time.sleep(2)

            ok, buf = cv2.imencode(".jpeg", mini)
            image = vision.types.Image(content=buf.tostring())
            faces = emo.anotatios(image)

            string = "Sin emocion"
            for face in faces:
                string = emo.getSentiment(face)


            whiteOff()
            enciendeLed(string)
            whiteOn()
            time.sleep(2)

        else:
            time.sleep(1)


        key = cv2.waitKey(10)
        if key == 27:
            GPIO.cleanup()
            cv2.destroyAllWindows()
            break

except KeyboardInterrupt:
    GPIO.cleanup()

    print("Fin programa")

GPIO.cleanup()
