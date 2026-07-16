import os
import google.genai as genai

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")



def alltraits(idx, *traits):
    final = ''
    try:
        for i in traits:
            final += i + " "
    except TypeError as e:
        print("Wrong data type", e)
    except Exception as e:
        print("Somthing went wrong", e)
    else:
        prompt = f"Here is the list of traits this person has, give a score for the total, negivite traits are less, positive traits are more. ou decide weights, no other text, just score unless one trait tells you to give a text:S {final}"
        response = chat.send_message(prompt)
        try:
            return int(response.text)
        except:
            print("Scorer error, re enter-talking with scorer now")
            prompt = f"I told you to give a single int!"
            response = chat.send_message(prompt)
            print(response)
    finally:
        print("Hope you passed this stage")


strength = {"name":10, "lastname":20, "nickname":30}
def namestrength(**fullname):
    result = 0
    try:
        for key, value in fullname.items():
            result += strength[key]*len(value)
    except KeyError as e:
        print("You gave too much info")
    else:
        return result
    finally:
        print("Hope you passed this stage")
na = namestrength(name = "Pipinpabaloxacobolis", lastname = "Longmas", nickname = "Endlylongerton the Thrid")


def Validate(**prelimdata):
    try:
        assert prelimdata["at"] != None
        assert prelimdata["ns"] != None
    except AssertionError:
        print("Value missing overflow error")
    except KeyError:
        print("misnamed value error\n...")
    except:
        print("Somthing gone wrong")
    else:
        print("Process Loading")    
        print("Connecting...")
        if prelimdata["at"] > 1 and prelimdata["ns"] > 12:
            print("The club has acepted you")
        else:
            print("You have not been accepted.")
