import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "18409823 ")) #optional
API_HASH = getenv("API_HASH", "aaba4d306e306a9f5b1eb7bf5ef8fe80" ) #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5754921368").split()))
OWNER_ID = int(getenv("OWNER_ID", "5754921368"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ri:ri@cluster0.091ue0h.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5839901251:AAF_y5uOpaavGGH_f7AuJV-ZaBilORm-GQo")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/tgramvn/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQEY6V8AvblrLo9XL9gyYGScRkhOVlWfdWfNLr76So6hww_FVziSbANlifnWovjcnxvQyqIyenkaSF-yVk7KAT8SBPbgSm2UjYaBC2D2oFodTk7T2mcXJr_hKj321sdH9G9Bltu0jjCUEWCs3S93ZrLTA_iBvXwgkumamtNSSuUEI293KhcN1-r4z1BdGG6bvL0481qDhGNPmbnB1hEoqONalH5Xk7-ROVwvlrWVT7F0XD9WNjWZefvrfecSo1tCa7aGZ6ZxMSWZwseOQ4TLvJtyAOnodaKpCdPci55AV6yIuGxcnyzye4Q8zj3X5fcLgcDB99GMMRal6lJ78sCUCy5cFBuHbwAAAAB0IwwQAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
