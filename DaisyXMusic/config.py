# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("NarutoXMusicPlayerBot", "session")
BOT_TOKEN = getenv("")
BOT_NAME = getenv("Naruto X Music Player")
UPDATES_CHANNEL = getenv("Narutoxmusicplayerchat")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {1}
API_ID = int(getenv("8522555", ""))
API_HASH = getenv("9e0b9e90b854c23fe89ee57b0a75ff32")
BOT_USERNAME = getenv("NarutoXMusicPlayerBot")
ASSISTANT_NAME = getenv("BigfatherRobot")
SUPPORT_GROUP = getenv("Narutoxmusicplayerchat")
PROJECT_NAME = getenv("NarutoXMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ToxicDeeModder1/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("UONGTV-YRNZJG-CLCGKM-YACOIH-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
