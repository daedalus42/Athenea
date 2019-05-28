"""
Google Vision API Tutorial with a Raspberry Pi and Raspberry Pi Camera.  See more about it here:  https://www.dexterindustries.com/howto/use-google-cloud-vision-on-the-raspberry-pi/
Use Google Cloud Vision on the Raspberry Pi to take a picture with the Raspberry Pi Camera and classify it with the Google Cloud Vision API.   First, we'll walk you through setting up the Google Cloud Platform.  Next, we will use the Raspberry Pi Camera to take a picture of an object, and then use the Raspberry Pi to upload the picture taken to Google Cloud.  We can analyze the picture and return labels (what's going on in the picture), logos (company logos that are in the picture) and faces.
This script uses the Vision API's label detection capabilities to find a label
based on an image's content.
"""



# [START tts_synthesize_text]
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16
        
        )
    
    response = client.synthesize_speech(input_text, voice, audio_config)

    with open('output12.wav', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
        #out.close()



def open_file(filename):
    subprocess.call('paplay '+str(filename), shell=True)
   # if sys.platform == "win32":
   #     os.startfile(filename)
   # else:
   #     opener ="open" if sys.platform == "darwin" else "xdg-open"
   #     subprocess.call([opener, filename])





def speak(text):
    synthesize_text(text)
   
    open_file('output12.wav')
    #time.sleep(5)




