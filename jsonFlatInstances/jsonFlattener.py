import json
import os

path = "../jsonInstances"

for directory in os.listdir(path):
    print("Działanie w folderze: " + directory + ".")
    combinedPath = os.path.join(path, directory)
    if os.path.isdir(combinedPath):
        try:
            os.mkdir(os.path.join(os.getcwd(), directory))
        except FileExistsError:
            pass
        except PermissionError:
            print(PermissionError)
        except Exception as e:
            print(e)
        for jsonPath in os.listdir(combinedPath):
            with open(os.path.join(combinedPath, jsonPath), "r") as jsonFile:
                jsonDict = json.load(jsonFile)
                flatJsonDict = {}
                for key, value in jsonDict.items():
                    if isinstance(value, dict):
                        for nestedKey, nestedValue in value.items():
                            flatJsonDict[nestedKey] = nestedValue
                    else:
                        flatJsonDict[key] = value
            with open(os.path.join(directory, jsonPath), "w") as flatJsonFile:
                flatJsonFile.write(json.dumps(flatJsonDict))
        
print("Gotowe.")