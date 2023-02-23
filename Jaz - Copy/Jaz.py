from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Initializing...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> All systems initialized")

def MainExecution():

    Speak("Hello Sir")

    while True:

        Data = MicExecution()
        Data = str(Data)
        
        if len(Data)<3:
            pass

        elif "turn on the tv" in Data: #Specific Command
           Speak = "Ok..Turning on the Andriod TV"

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!!")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()