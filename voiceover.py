import configparser
import pyttsx3

# voiceoverDir = "Voiceovers"
# voiceoverDir = "C:\\Users\\srcol\\Videos\\temp"

def create_voice_over(fileName, text):
    config = configparser.ConfigParser()
    config.read('config.ini')
    voiceoverDir = config["General"]["TemporalDir"]
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    # for voice in voices:
    #     print(voice.id, voice.name)     #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[4].id)   #changing index, changes voices. 1 for female
    # for voice in voices:
    #     if len(voice.languages) > 0 and "spanish" in voice.languages[0]:
    #         engine.setProperty('voice', voice.id)
    #         break
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath