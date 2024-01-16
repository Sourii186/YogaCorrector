import pyttsx3


class speak:

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(text)
        engine.runAndWait()

    def instruct_user(index):
        body_parts = {
            0: "left elbow",
            1: "right elbow",
            2: "right knee",
            3: "left knee",
            4: "right shoulder",
            5: "left shoulder",
            6: "left hip",
            7: "right hip"
        }

        if index == -1:
            speak("Hold the position and focus on your breathing.")
        elif index in body_parts:
            body_part = body_parts[index]
            speak(f"Please straighten your {body_part}. Focus on maintaining a comfortable angle.")
