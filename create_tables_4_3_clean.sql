CREATE TABLE armoritems (
    itemid TEXT,
    armor TEXT,
    luck FLOAT,
    intelligence FLOAT,
    constitution FLOAT,
    agility FLOAT,
    strength FLOAT
);

CREATE TABLE backpacks (
    playerid TEXT,
    itemid TEXT,
    slot TEXT
);

CREATE TABLE equippeditems (
    characterid TEXT,
    itemid TEXT,
    slot TEXT
);

CREATE TABLE genericitems (
    itemid TEXT,
    name TEXT,
    level TEXT,
    type TEXT,
    classtypebelonging TEXT,
    rarity TEXT,
    gold FLOAT,
    mushrooms FLOAT
);

CREATE TABLE guildattacks (
    attackingguildid TEXT,
    defendingguildid TEXT,
    attacktime TIMESTAMP
);

CREATE TABLE guildmemberships (
    characterid TEXT,
    guildid TEXT,
    role TEXT
);

CREATE TABLE guilds (
    guildid TEXT,
    name TEXT,
    region TEXT,
    nr TEXT,
    glory TEXT,
    trainerlevel TEXT,
    treasurylevel TEXT
);

CREATE TABLE playeraccounts (
    accountid TEXT,
    login TEXT,
    email TEXT,
    password TEXT
);

CREATE TABLE playercharacters (
    characterid TEXT,
    accountid TEXT,
    name TEXT,
    region TEXT,
    nr TEXT,
    level TEXT,
    exp TEXT,
    characterclass TEXT,
    race TEXT,
    owngold TEXT,
    ownmushrooms TEXT,
    glory TEXT,
    strength TEXT,
    agility TEXT,
    intelligence TEXT,
    constitution TEXT,
    luck TEXT,
    hp TEXT
);

CREATE TABLE potionaffectedcharacters (
    characterid TEXT,
    itemid TEXT,
    expirytime TIMESTAMP
);

CREATE TABLE potionitems (
    itemid TEXT,
    effecttype TEXT,
    potency TEXT,
    duration TEXT
);

CREATE TABLE quests (
    questid TEXT,
    name TEXT,
    goal TEXT,
    goalsdonerequired TEXT,
    traveltime TIMESTAMP,
    goldreward TEXT,
    expreward TEXT
);

CREATE TABLE questsinprogress (
    questid TEXT,
    characterid TEXT,
    goalsdone TEXT,
    travelendtime TIMESTAMP
);

CREATE TABLE shopoffers (
    playerid TEXT,
    itemid TEXT,
    shop TEXT,
    slot TEXT
);

CREATE TABLE weaponitems (
    itemid TEXT,
    damage TEXT,
    luck FLOAT,
    intelligence FLOAT,
    strength FLOAT,
    constitution FLOAT,
    agility FLOAT
);

