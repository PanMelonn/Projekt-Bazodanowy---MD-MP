import uuid
import json
import random
import os
import datetime
from math import ceil
from faker import Faker

faker = Faker()

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
    
    print("Generated " + str(i - 1) + " account json files.")

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
    
    print("Generated " + str(i - 1) + " quest json files.")

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
            jsonDict = {"guildId": str(id),
                        "name": name.strip(),
                        "world": worldDict,
                        "glory": glory,
                        "trainerLevel": trainerLevel,
                        "treasuryLevel": treasuryLevel}
            with open("../jsonInstances/guilds/guild" + str(i) + ".json", "w") as guildFile:
                guildFile.write(json.dumps(jsonDict))
                i += 1
    
    print("Generated " + str(i - 1) + " guild json files.")

def guildAttackGen():
    i = 1
    guildIdsDict = {}
    try:
        os.mkdir("../jsonInstances/guildAttacks/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    for filename in os.listdir("../jsonInstances/guildAttacks/"):
        filePath = os.path.join("../jsonInstances/guildAttacks/", filename)
        if os.path.isfile(filePath):
            os.remove(filePath)
    
    for guildFiles in os.listdir("../jsonInstances/guilds/"):
        with open(os.path.join("../jsonInstances/guilds/", guildFiles), "r") as guildFile:
            guildDict = json.load(guildFile)
            guildId = guildDict["guildId"]
            guildRegion = guildDict["world"]["region"]
            guildNr = guildDict["world"]["nr"]
            guildIdsDict.setdefault((guildRegion, guildNr), []).append(guildId)
    
    for guildId in guildIdsDict.keys():
        attackCandidates = guildIdsDict[guildId].copy()
        defenceCandidates = guildIdsDict[guildId].copy()
        while len(attackCandidates) != 0 or not len(defenceCandidates) != 0:
            attacker = random.choice(attackCandidates)
            if random.random() >= 0.75:
                defender = random.choice(defenceCandidates)
                time = faker.date_time_between(start_date=datetime.datetime.now(), end_date='+1d')
                with open("../jsonInstances/guildAttacks/guildAttack" + str(i) + ".json", "w") as file:
                    jsonDict = {"attackingGuildId": attacker,
                                "defendingGuildId": defender,
                                "attackTime": str(time)}
                    file.write(json.dumps(jsonDict))
                i += 1
                defenceCandidates.remove(defender)
            attackCandidates.remove(attacker)
    
    print("Generated " + str(i - 1) + " guild attacks json files.")

def genericItemGen():
    i = 1
    rarities = ["common", "epic", "legendary"]
    classBelongings = ["ranged", "melee", "magic"]
    try:
        os.mkdir("../jsonInstances/genericItems/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    with open("meleeWeaponNames.txt", "r") as nameFile:
        for name in nameFile:
            id = uuid.uuid4()
            level = random.randint(1, 300)
            rarity = random.choice(rarities)
            jsonDict = {"itemId": str(id),
                        "name": name.strip(),
                        "level": level,
                        "type": "weapon",
                        "classTypeBelonging": "melee",
                        "rarity": rarity}
            with open("../jsonInstances/genericItems/genericItem" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
    
    with open("rangedWeaponNames.txt", "r") as nameFile:
        for name in nameFile:
            id = uuid.uuid4()
            level = random.randint(1, 300)
            rarity = random.choice(rarities)
            jsonDict = {"itemId": str(id),
                        "name": name.strip(),
                        "level": level,
                        "type": "weapon",
                        "classTypeBelonging": "ranged",
                        "rarity": rarity}
            with open("../jsonInstances/genericItems/genericItem" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
    
    with open("magicWeaponNames.txt", "r") as nameFile:
        for name in nameFile:
            id = uuid.uuid4()
            level = random.randint(1, 300)
            rarity = random.choice(rarities)
            jsonDict = {"itemId": str(id),
                        "name": name.strip(),
                        "level": level,
                        "type": "weapon",
                        "classTypeBelonging": "magic",
                        "rarity": rarity}
            with open("../jsonInstances/genericItems/genericItem" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
    
    armorTypes = ["armors", "belts", "boots", "gloves", "helmets", "necklaces", "rings", "trinkets", "shields"]
    SingularArmorTypes = ["armor", "belt", "boots", "gloves", "helmet", "necklace", "ring", "trinket", "shield"]
    for armorType, SingularArmorType in zip(armorTypes, SingularArmorTypes):
        with open(armorType + ".txt", "r") as nameFile:
            for name in nameFile:
                id = uuid.uuid4()
                level = random.randint(1, 300)
                rarity = random.choice(rarities)
                classBelonging = random.choice(classBelongings)
                jsonDict = {"itemId": str(id),
                            "name": name.strip(),
                            "level": level,
                            "type": SingularArmorType,
                            "classTypeBelonging": classBelonging,
                            "rarity": rarity}
                with open("../jsonInstances/genericItems/genericItem" + str(i) + ".json", "w") as file:
                    file.write(json.dumps(jsonDict))
                    i += 1
    
    with open("potions.txt", "r") as nameFile:
            for name in nameFile:
                id = uuid.uuid4()
                level = random.randint(1, 300)
                rarity = random.choice(rarities)
                classBelonging = random.choice(classBelongings)
                jsonDict = {"itemId": str(id),
                            "name": name.strip(),
                            "level": level,
                            "type": "potion",
                            "rarity": rarity}
                with open("../jsonInstances/genericItems/genericItem" + str(i) + ".json", "w") as file:
                    file.write(json.dumps(jsonDict))
                    i += 1
    
    print("Generated " + str(i - 1) + " generic item json files.")

def weaponItemGen():
    i = 1
    weapons = []
    try:
        os.mkdir("../jsonInstances/weaponItems/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    possibleStats = ["strength", "agility", "intelligence", "constitution", "luck"]
    
    for genericItem in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", genericItem), "r") as file:
            genericItemDict = json.load(file)
            if genericItemDict["type"] == "weapon":
                weapons.append([genericItemDict["itemId"], genericItemDict["level"]])
    
    for weapon in weapons:
        id = weapon[0]
        level = weapon[1]
        with open("../jsonInstances/weaponItems/weaponItem" + str(i) + ".json", "w") as file:
            statsAmount = random.randint(0, len(possibleStats))
            statsPresent = random.sample(possibleStats, statsAmount)
            damage = level * 5 + random.randint(0, 30)
            statsDict = {"damage": damage}
            for stat in statsPresent:
                statsDict[stat] = level * 5 + random.randint(0, 50)
            jsonDict = {"itemId": str(id),
                    "statistics": statsDict}
            file.write(json.dumps(jsonDict))
            i += 1
    
    print("Generated " + str(i - 1) + " weapon item json files.")

def armorItemGen():
    i = 1
    armors = []
    try:
        os.mkdir("../jsonInstances/armorItems/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    possibleStats = ["strength", "agility", "intelligence", "constitution", "luck"]
    
    for genericItem in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", genericItem), "r") as file:
            genericItemDict = json.load(file)
            if genericItemDict["type"] in ["armor", "belt", "boots", "gloves", "helmet", "necklace", "ring", "trinket", "shield"]:
                armors.append([genericItemDict["itemId"], genericItemDict["level"]])
    
    for armor in armors:
        id = armor[0]
        level = armor[1]
        with open("../jsonInstances/armorItems/armorItem" + str(i) + ".json", "w") as file:
            statsAmount = random.randint(0, len(possibleStats))
            statsPresent = random.sample(possibleStats, statsAmount)
            armor = level * 5 + random.randint(0, 30)
            statsDict = {"armor": armor}
            for stat in statsPresent:
                statsDict[stat] = level * 5 + random.randint(0, 50)
            jsonDict = {"itemId": str(id),
                    "statistics": statsDict}
            file.write(json.dumps(jsonDict))
            i += 1
    
    print("Generated " + str(i - 1) + " armor item json files.")

def potionItemGen():
    i = 1
    potions = []
    try:
        os.mkdir("../jsonInstances/potionItems/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    possibleStats = ["strength", "agility", "intelligence", "constitution", "luck"]
    
    for genericItem in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", genericItem), "r") as file:
            genericItemDict = json.load(file)
            if genericItemDict["type"] == "potion":
                potions.append([genericItemDict["itemId"], genericItemDict["level"]])
    
    for potion in potions:
        id = potion[0]
        level = potion[1]
        with open("../jsonInstances/potionItems/potionItem" + str(i) + ".json", "w") as file:
            stat = random.choice(possibleStats)
            potency = int(ceil(level / 5))
            duration = 60 * level
            jsonDict = {"itemId": str(id),
                    "effectType": stat,
                    "potency": potency,
                    "duration": duration}
            file.write(json.dumps(jsonDict))
            i += 1

    print("Generated " + str(i - 1) + " potion item json files.")

def playerCharacterGen():
    i = 1
    accountIdPtr = 0
    regions = ["int", "eu", "am", "cz", "pl", "de", "fr", "hu"]
    characterClasses = ["warrior", "mage", "scout", "assasin", "battleMage", "berserker", "druid", "demonHunter", "bard"]
    races = ["human", "elf", "dwarf", "gnome", "orc", "darkElf", "goblin", "demon"]
    try:
        os.mkdir("../jsonInstances/playerCharacters/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    accountIds = []
    
    for account in os.listdir("../jsonInstances/playerAccounts/"):
        with open(os.path.join("../jsonInstances/playerAccounts/", account), "r") as file:
            jsonDict = json.load(file)
            accountIds.append(jsonDict["accountId"])
    
    accountIdsLength = len(accountIds)
    
    with open("playerNames.txt", "r") as playerNamesFile:
        for name in playerNamesFile:
            id = uuid.uuid4()
            worldDict = {"region": random.choice(regions),
                        "nr": random.randint(1, 2)}
            level = random.randint(1, 500)
            exp = random.randint(0, level *  1000)
            characterClass = random.choice(characterClasses)
            race = random.choice(races)
            ownGold = random.randint(0, level * 100)
            ownMushrooms = random.randint(0, level * 10)
            glory = random.randint(0, level * 100)
            stats = ["strength", "agility", "intelligence", "constitution", "luck"]
            baseStatistics = {}
            for stat in stats:
                baseStatistics[stat] = random.randint(1, level * 30)
            baseStatistics["hp"] = random.randint(level * 1000, level * 10000)
            
            jsonDict = {"characterId": str(id),
                        "accountId": accountIds[accountIdPtr],
                        "name": name.strip(),
                        "world": worldDict,
                        "level": level,
                        "exp": exp,
                        "characterClass": characterClass,
                        "race": race,
                        "ownGold": ownGold,
                        "ownMushrooms": ownMushrooms,
                        "glory": glory,
                        "baseStatistics": baseStatistics}
            with open("../jsonInstances/playerCharacters/playerCharacter" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
            if random.random() < 0.7:
                accountIdPtr += 1
            if accountIdPtr >= accountIdsLength:
                break
    
    print("Generated " + str(i - 1) + " player character json files.")

def potionAffectedCharacterGen():
    i = 1
    try:
        os.mkdir("../jsonInstances/potionAffectedCharacters/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    characters = {}
    potions = {} #keys - id, values - [level, duration]
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as file:
            characterDict = json.load(file)
            characters[characterDict["characterId"]] = characterDict["level"]
    
    for item in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", item), "r") as file:
            itemDict = json.load(file)
            if itemDict["type"] == "potion":
                potions.setdefault(itemDict["itemId"], []).append(itemDict["level"])
    
    for potion in os.listdir("../jsonInstances/potionItems/"):
        with open(os.path.join("../jsonInstances/potionItems/", potion), "r") as file:
            potionDict = json.load(file)
            potions[potionDict["itemId"]].append(potionDict["duration"])
    
    for characterId in characters.keys():
        if random.random() < 0.7:
            continue 
        potionIds = [k for k in potions.keys() if potions[k][0] <= characters[characterId]]
        potionId = random.choice(potionIds)
        duration = potions[potionId][1]
        expiryTime = faker.date_time_between(start_date=datetime.datetime.now(), end_date="+" + str(duration) + "s")
        jsonDict = {"characterId": characterId,
                    "itemId": potionId,
                    "expiryTime": str(expiryTime)}
        with open("../jsonInstances/potionAffectedCharacters/potionAffectedCharacter" + str(i) + ".json", "w") as file:
            file.write(json.dumps(jsonDict))
            i += 1
    
    print("Generated " + str(i - 1) + " potion affected character json files.")

def questInProgressGen():
    i = 1
    try:
        os.mkdir("../jsonInstances/questsInProgress/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    quests = []
    
    for quest in os.listdir("../jsonInstances/quests/"):
        with open(os.path.join("../jsonInstances/quests/", quest), "r") as file:
            itemDict = json.load(file)
            quests.append([itemDict["questId"], itemDict["goalsDoneRequired"], itemDict["travelTime"]])
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        if random.random() < 0.5:
            continue
        quest = random.choice(quests)
        questId = quest[0]
        goalsDone = random.randint(1, quest[1])
        travelEndTime = str(faker.date_time_between(start_date=datetime.datetime.now(), end_date="+" + str(quest[2]) + "s"))
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as charFile:
            characterDict = json.load(charFile)
            characterId = characterDict["characterId"]
            jsonDict = {"questId": questId,
                        "characterId": characterId,
                        "goalsDone": goalsDone,
                        "travelEndTime": travelEndTime}
            with open("../jsonInstances/questsInProgress/questInProgress" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
    
    print("Generated " + str(i - 1) + " quest in progress json files.")

def guildMembershipGen():
    i = 1
    guilds = {} #keys - (region, nr), values - ids
    characters = {} # - (region, nr), values - ids
    try:
        os.mkdir("../jsonInstances/guildMemberships/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as file:
            characterDict = json.load(file)
            characters.setdefault((characterDict["world"]["region"], characterDict["world"]["nr"]), []).append(characterDict["characterId"])
    
    for guild in os.listdir("../jsonInstances/guilds/"):
        with open(os.path.join("../jsonInstances/guilds/", guild), "r") as file:
            guildDict = json.load(file)
            guilds.setdefault((guildDict["world"]["region"], guildDict["world"]["nr"]), []).append(guildDict["guildId"])

    for world in guilds.keys():
        j = 0
        worldGuilds = guilds[world]
        leadersLimit = len(worldGuilds)
        officersLimit = 3 * leadersLimit
        worldCharacters = characters[world]
        while len(worldCharacters) != 0:
            guildId = worldGuilds[j % leadersLimit]
            characterId = random.choice(worldCharacters)
            if j < leadersLimit:
                role = "leader"
            elif j < officersLimit:
                role = "officer"
            else:
                rand = random.random() 
                if rand > 0.9:
                    role = "officer"
                elif rand < 0.2:
                    worldCharacters.remove(characterId)
                    continue
                else:
                    role = "member"
            jsonDict = {"characterId": characterId,
                        "guildId": guildId,
                        "role": role}
            with open("../jsonInstances/guildMemberships/guildMembership" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
                j += 1
                worldCharacters.remove(characterId)
    
    print("Generated " + str(i - 1) + " guild membership json files.")

def backpackGen():
    i = 1
    characters = []
    items = []
    try:
        os.mkdir("../jsonInstances/backpacks/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as file:
            characterDict = json.load(file)
            characters.append(characterDict["characterId"])
    
    for item in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", item), "r") as file:
            itemDict = json.load(file)
            items.append(itemDict["itemId"])
    
    for character in characters:
        remainingSlots = [i for i in range(1, 11)]
        slot = random.choice(remainingSlots)
        itemId = random.choice(items)
        jsonDict = {"playerId": character,
                    "itemId": itemId,
                    "slot": slot}
        with open("../jsonInstances/backpacks/backpack" + str(i) + ".json", "w") as file:
            file.write(json.dumps(jsonDict))
            i += 1
        remainingSlots.remove(slot)
        chance = 0.1
        while random.random() >= chance:
            slot = random.choice(remainingSlots)
            itemId = random.choice(items)
            jsonDict = {"playerId": character,
                        "itemId": itemId,
                        "slot": slot}
            with open("../jsonInstances/backpacks/backpack" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
            remainingSlots.remove(slot)
            chance += 0.15
    
    print("Generated " + str(i - 1) + " backpack json files.")

def equippedItemGen():
    i = 1
    characters = {}
    items = {}
    weapons = {}
    itemClassTypeBelongingToCharacterClass = {"melee": ("warrior", "assasin", "berserker", "battleMage"),
                                            "ranged": ("scout", "demonHunter"),
                                            "magic": ("mage", "druid", "bard")}
    try:
        os.mkdir("../jsonInstances/equippedItems/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as file:
            characterDict = json.load(file)
            characters.setdefault((characterDict["characterClass"], characterDict["level"]), []).append(characterDict["characterId"])
    
    for item in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", item), "r") as file:
            itemDict = json.load(file)
            if itemDict.get("classTypeBelonging") != None:
                items.setdefault((itemDict["classTypeBelonging"], itemDict["type"], itemDict["level"]), []).append(itemDict["itemId"])
    
    for characterKey in characters.keys():
        characterItems = {}
        for characterItemKey in items.keys():
            if characterKey[0] in itemClassTypeBelongingToCharacterClass[characterItemKey[0]]:
                characterItems.setdefault((characterItemKey[1], characterItemKey[2]), []).extend(items[characterItemKey])
        itemTypes = ["helmet", "armor", "gloves", "boots", "necklace", "belt", "ring", "trinket", "weapon"]
        if characterKey[0] == "warrior":
            itemTypes.append("shield")
        elif characterKey[0] == "assasin":
            itemTypes.append("weapon")
        for character in characters[characterKey]:
            leftHandNotUsed = True
            for itemType in itemTypes:
                if random.random() > 0.9:
                    continue
                slotItems = []
                for levelItemKey in characterItems.keys():
                    if levelItemKey[0] == itemType and levelItemKey[1] <= characterKey[1]:
                        slotItems.extend(characterItems[levelItemKey])
                
                if len(slotItems) == 0:
                    continue
                itemId = random.choice(slotItems)
                if itemType != "weapon":
                    slot = itemType
                elif itemType == "weapon" and leftHandNotUsed:
                    slot = "leftHand"
                    leftHandNotUsed = False
                else:
                    slot = "rightHand"
                jsonDict = {"characterId": character,
                            "itemId": itemId,
                            "slot": slot}
                with open("../jsonInstances/equippedItems/equippedItem" + str(i) + ".json", "w") as file:
                    file.write(json.dumps(jsonDict))
                    i += 1
    
    print("Generated " + str(i - 1) + " equipped items json files.")

def shopOfferGen():
    i = 1
    characters = {}
    armsShopItems = {}
    magicShopItems = {}
    try:
        os.mkdir("../jsonInstances/shopOffers/")
    except FileExistsError:
        pass
    except PermissionError:
        print(PermissionError)
    except Exception as e:
        print(e)
    
    for character in os.listdir("../jsonInstances/playercharacters/"):
        with open(os.path.join("../jsonInstances/playercharacters/", character), "r") as file:
            characterDict = json.load(file)
            characters[characterDict["characterId"]] = characterDict["level"]
    
    for item in os.listdir("../jsonInstances/genericItems/"):
        with open(os.path.join("../jsonInstances/genericItems/", item), "r") as file:
            itemDict = json.load(file)
            if itemDict["type"] in ("weapon", "armor", "belt", "boots", "gloves", "helmet", "shield"):
                armsShopItems.setdefault(itemDict["level"], []).append(itemDict["itemId"])
            else:
                armsShopItems.setdefault(itemDict["level"], []).append(itemDict["itemId"])
    
    for character in characters.items():
        characterArmsShopItems = []
        characterMagicShopItems = []
        
        for items in armsShopItems.items():
            if items[0] <= character[1]:
                characterArmsShopItems.extend(items[1])
        
        for items in magicShopItems.items():
            if items[0] <= character[1]:
                characterMagicShopItems.extend(items[1])
        
        for j in range(1, 7):
            if len(characterArmsShopItems) == 0:
                break
            item = random.choice(characterArmsShopItems)
            jsonDict = {"playerId": character[0],
                        "itemId": item,
                        "shop": "arms",
                        "slot": j}
            with open("../jsonInstances/shopOffers/shopOffers" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
        
        for j in range(1, 7):
            if len(characterMagicShopItems) == 0:
                break
            item = random.choice(characterMagicShopItems)
            jsonDict = {"playerId": character[0],
                        "itemId": item,
                        "shop": "magic",
                        "slot": j}
            with open("../jsonInstances/shopOffers/shopOffers" + str(i) + ".json", "w") as file:
                file.write(json.dumps(jsonDict))
                i += 1
    
    print("Generated " + str(i - 1) + " shop offer json files.")

accountGen()
questGen()
guildGen()
guildAttackGen()
genericItemGen()
weaponItemGen()
armorItemGen()
potionItemGen()
playerCharacterGen()
potionAffectedCharacterGen()
questInProgressGen()
guildMembershipGen()
backpackGen()
equippedItemGen()
shopOfferGen()