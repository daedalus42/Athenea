
# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# See http://g.co/cloud/speech/docs/languages
# for a list of supported languages.
language_code = 'en-US'  # a BCP-47 language tag

client = speech.SpeechClient()
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code=language_code)
streaming_config = types.StreamingRecognitionConfig(
    config=config,
    interim_results=True)
"""
respuestas_afirmative = ["yes", "okey", "its fine","yeah","why not","sure"]
respuestas_negative = ["no", "nah", "stop","not again"]
respuestas_chiste_knock1 = ["who's there","who is there"]
respuestas_chiste_knock2 = ["who"]
afirmative_re = '|'.join(respuestas_afirmative)
negative_re = '|'.join(respuestas_negative)
chiste_knock1_re = '|'.join(respuestas_chiste_knock1)
chiste_knock2_re = '|'.join(respuestas_chiste_knock2)
"""

def listen(stream):
        stream.reset()
        
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)
    
        responses = client.streaming_recognize(streaming_config, requests)

        transcripts_final = st.SpeechToText(responses,stream)

	#print("---TRANSC_FINAL:")
        if len(transcripts_final)!=0:
            print(transcripts_final[0])
        return transcripts_final


def question_answer(Q,stream):
    while True:
        print(Q)
        transcripts = listen(stream)
        
        if len(transcripts) == 0:
            print ("I didn't understand you.")
        else:
            break
        
    return transcripts
    
    

def Owl_joke():
    with ms.MicrophoneStream(RATE, CHUNK) as stream:
    
        tipo_answer = 0
        while True:
            question = "Do you want me to tell you a joke?"
            tts.speak(question)
            transcripts = question_answer(question,stream)
           
            #afirmative_re = "\b(yes|why not)\b"
            #print (transcripts)
            if re.search(r'\b(okey|yeah|yes)\b', transcripts[0], re.I):
                break
            elif re.search(r"\b(no|nah|stop|not again)\b", transcripts[0], re.I): 
                tipo_answer = 1
                
                break
            else: 
                print ("Answer with yes or no please")
                tts.speak("Answer with yes or no please")
                time.sleep(1)
                
        if tipo_answer==0:
            while True:
                q = "Knock Knock"
                tts.speak(q)
                transcripts = question_answer(q,stream)
                if re.search(r"\b(who's there|who is there)\b", transcripts[0], re.I):
                    break
                else:
                    print ("Wrong answer, ask me who is there")
                    tts.speak("Wrong answer, ask me who is there")
            while True:
                q = "Owls say "
                tts.speak(q)
                transcripts = question_answer(q,stream)
                if re.search(r"\b(who|Owls say hoo)\b", transcripts[0], re.I):
                    break
                else:
                    print ("Wrong answer")
                    tts.speak("Wrong answer")
                    time.sleep(1)
            print ("Yes, they do")
            tts.speak("Yes, they do")
            time.sleep(0.5)
            print ("Hoo Hoo")
            tts.speak("Hoo Hoo")
            time.sleep(0.5)
            tts.speak("Hoo Hoo")
            time.sleep(0.5)
            while True:
                q = "Did you like it?"
                tts.speak(q)
                transcripts = question_answer(q,stream)
                if re.search(r"\b(yes)\b", transcripts[0], re.I):
                    break
                elif re.search(r"\b(no)\b", transcripts[0], re.I): 
                    tipo_answer = 2
                    break
                else: 
                    print ("Answer with yes or no please")
                    tts.speak("Answer with yes or no please")
                    time.sleep(1)
       
        if tipo_answer==0:
            print ("Cool, I like you too")
            tts.speak("Cool, I like you too")
        elif tipo_answer == 2:
            print("Sorry, I guess I am really bad telling Jokes")
            tts.speak("Sorry, I guess I am really bad telling Jokes")
        else: 
            print("You are a bad person.")
            tts.speak("You are a bad person.")
            

def select_color():
    with ms.MicrophoneStream(RATE, CHUNK) as stream:
        q = "Choose a color, between red, green, blue and purple."
        tts.speak(q)
        transcripts = question_answer(q,stream)
        if re.search(r"\b(red)\b", transcripts[0], re.I):
            return 1
        elif re.search(r"\b(green)\b", transcripts[0], re.I): 
            return 2
        elif re.search(r"\b(purple)\b", transcripts[0], re.I):
            return 3
        elif re.search(r"\b(blue)\b", transcripts[0], re.I):
            return 4
        else: 
            return 0

def listenAnswer():
    with ms.MicrophoneStream(RATE, CHUNK) as stream:
        return listen(stream)

# Now, put the transcription responses to use.

