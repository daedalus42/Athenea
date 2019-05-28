# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:35:54 2019

@author: Apocalipto
"""



def get_current_time():
    return int(round(time.time() * 1000))

def SpeechToText(responses,stream):
    print("STT-----------------------------start")
    
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    transcripts = []
    num_chars_printed = 0

    for response in responses:
        print("ENTRO")
        print("STT it")
        print("results: ", response.results)
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript
        stream.start_time = get_current_time()
        
        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))
        
        if not result.is_final:

            #sys.stdout.write(transcript + overwrite_chars + '\r')
            
            #sys.stdout.flush()

            num_chars_printed = len(transcript)
            #print (" NO ES final\n")

        else:
            
            transcripts.append(transcript)
            
            #print (" over: " + overwrite_chars)
            #print(" ES Final\n")
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(quit|yes|who's there|owls say hoo|no|who|spell|red|blue|purple|green)\b", transcript, re.I):
                
                #print (re.search(r'\b(knock knock|quit|what the fuck)\b', transcript, re.I).group())
                #print('Exiting..')
                break

            num_chars_printed = 0
            
    #print("STT-----------------------------end")
    return transcripts
