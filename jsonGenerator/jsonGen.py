import uuid
import json
import random
import os
import faker

def accountGen():
    with open("logins.txt", "r") as loginsFile, \
    open("emails.txt", "r") as emailsFile, \
    open("passwords.txt", "r") as passwordsFile:
        try:
            os.mkdir("../jsonInstances/playerAccounts")
        except FileExistsError:
            pass
        except PermissionError:
            print("Brak permisji do stworzenia potrzebnego folderu.")
        except Exception as e:
            print("Błąd stworzenia folderu.")
        i = 1
        for login, email, password in zip(loginsFile, emailsFile, passwordsFile):
            with open("../jsonInstances/playerAccounts/playerAccount" + str(i) + ".json", "w") as playerAccountFile:
                id = uuid.uuid4()
                jsonDict = {"accountId": str(id),
                            "login": login.strip(),
                            "email": email.strip(),
                            "password": password.strip()}
                jsonObject = json.dumps(jsonDict)
                playerAccountFile.write(jsonObject)
                i += 1

def questGen():
    with open("questNames.txt", "r") as questNamesFile, \
    open("enemiesNames.txt", "r") as enemiesNamesFile:
        i = 1
        try:
            os.mkdir("../jsonInstances/quests/")
        except FileExistsError:
            pass
        except PermissionError:
            print(PermissionError)
        except Exception as e:
            print(e)
        for questName, enemyName in zip(questNamesFile, enemiesNamesFile):
            with open("../jsonInstances/quests/quests" + str(i) + ".json", "w") as questFile:
                id = uuid.uuid4()
                goalsDoneRequired = random.randint(1, 10)
                travelTime = random.randint(15, 600)
                goldReward = random.randint(0, 2000)
                expReward = random.randint(0, 20000)
                jsonDict = {"questId": str(id),
                            "name": questName.strip(),
                            "goal": enemyName.strip(),
                            "goalsDoneRequired": goalsDoneRequired,
                            "travelTime": travelTime,
                            "goldReward": goldReward,
                            "expReward": expReward}
                jsonObject = json.dumps(jsonDict)
                questFile.write(jsonObject)
                i += 1

def guildGen():
    i = 1
    regions = ["int", "eu", "am", "cz", "pl", "de", "fr", "hu"]
    with open("guildNames.txt", "r") as guildNamesFile:
        try:
            os.mkdir("../jsonInstances/guilds/")
        except FileExistsError:
            pass
        except PermissionError:
            print(PermissionError)
        except Exception as e:
            print(e)
        for name in guildNamesFile:
            id = uuid.uuid4()
            worldNr = random.randint(1, 2)
            worldDict = {"region": random.choice(regions),
                        "nr": worldNr}
            glory = random.randint(1, 10000)
            trainerLevel = random.randint(1, 1000)
            treasuryLevel = random.randint(1, 1000)
            jsonDict = {"guildId": id,
                        "name": name.strip(),
                        "world": worldDict,
                        "glory": glory,
                        "trainerLevel": trainerLevel,
                        "treasuryLevel": treasuryLevel}
            with open("../jsonInstances/guilds/guild" + str(i) + ".json", "w") as guildFile:
                guildFile.write(jsonDict)

def guildAttackGen():
    i = 1
    j = 1600
    regions = ["int", "eu", "am", "cz", "pl", "de", "fr", "hu"]
    guildIds = []
    for region in regions:
        for nr in range(1, 3):
            for guildFiles in os.listdir("../jsonInstances/guilds/"):
                with open(os.path.join("../jsonInstances/guilds/", guildFiles), "r") as guildFile:
                    jsonDict = json.load(guildFile)
                    if jsonDict["world"]["region"] == region and jsonDict["world"]["nr"] == nr:
                        