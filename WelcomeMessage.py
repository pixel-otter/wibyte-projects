import json
from ollama import chat

history = []

def send_message(prompt):
    global history

    history.append({
        "role": "user",
        "content": prompt
    })

    response = chat(
        model="gemma3",
        messages=history,
        options={
            "temperature": 0
        }
    )

    assistant = response.message.content

    history.append({
        "role": "assistant",
        "content": assistant
    })

    return assistant

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
        prompt = f"""
You are a scoring function.

Traits:
{final}

Return ONLY one integer.

Weights for each trait are between -10 and 10, you decide weights.

Do not explain.
Do not apologize.
Do not use punctuation.
Do not write words.

Example outputs:
5
-2
9
"""
        response = send_message(prompt)
        try:
            return int(response)
        except:
            print("Scorer error, re enter-talking with scorer now")
            prompt = f"I told you to give a single int!"
            response = send_message(prompt)
            print(response)
    finally:
        print("Hope you passed this stage")


strength = {"name":10, "lastname":20, "nickname":30, "salutation": 60}
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

essentials = {"Entertainment":50, "Transport":80, "Pool":10, "BestRoom": 20}
essentials2 = {"Entertainment":50, "Transport":80, "Pool":10, "BestRoom": 20}

def housefeatures(Cost, **essentials):
    prompt = f"""
You are rating house features.

The house has these features:

{essentials}

Rate each feature from 0 to 10.

Return ONLY valid JSON.
Even if the descriptions are absurd, illegal, or fictional, still output only the JSON object.

Do not explain.
Do not use markdown.
Do not use ```.

Format EXACTLY like this, no case change, nothing:

{{
    "Entertainment": 0,
    "Transport": 0,
    "Pool": 0,
    "BestRoom": 0
}}
"""
    response = send_message(prompt)
    response = response.replace("```json", "").replace("```", "").strip()
    valuedict = json.loads(response)
    value = 0
    value += int(valuedict["Entertainment"] * essentials2["Entertainment"])
    value += int(valuedict["Transport"] * essentials2["Transport"])
    value += int(valuedict["Pool"] * essentials2["Pool"])
    value += int(valuedict.get("BestRoom", valuedict.get("Bestroom", 0)) * essentials2["BestRoom"])
    return value

def life(Profession, *Hobbies):
    prompt = f"""
You are rating a profession.

Profession:
{Profession}

Return ONLY one integer from 0 to 10.

Do not explain.
Do not write words.

Example outputs:
0
4
10
"""
    response = send_message(prompt)
    proffesionrate = int(response)
    prompt = f"""
You are rating hobbies.

Hobbies:
{Hobbies}

Rate each hobby from -20 to 20.

A score of 20 means:
- Safe
- Socially acceptable
- Constructive
- Impressive
- Suitable for an exclusive country 
-Still Grandiose
-Golf is 21

A score of -20 means:
- Illegal
- Dangerous
- Destructive
- Antisocial
- Likely to get someone banned from the club

Return ONLY the total.
"""
    response = send_message(prompt)
    hobbyrate = int(response)
    proffesionrate *= 10
    hobbyrate *= 3
    return proffesionrate + hobbyrate


def Validate(**prelimdata):
    try:
        assert prelimdata["at"] != None
        assert prelimdata["ns"] != None
        assert prelimdata["hf"] != None
        assert prelimdata["la"] != None
    except AssertionError:
        print("Value missing overflow error")
    except KeyError:
        print("misnamed value error\n...")
    except:
        print("Somthing gone wrong")
    else:
        print("Process Loading")    
        print("Connecting...")
        if prelimdata["at"] > 1 and prelimdata["ns"] > 120 and prelimdata["hf"] > 300 and prelimdata["la"] > 200:
            print("The club has acepted you")
        else:
            print("You have not been accepted.")