import uuid
import json

with open("logins.txt", "r") as loginsFile, \
open("emails.txt", "r") as emailsFile, \
open("passwords.txt", "r") as passwordsFile:
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