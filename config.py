# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

import os


class Config(object)
import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "21414281"))
    API_HASH = os.environ.get("API_HASH", "le3d0118e681d5a1eb139c5f634e9eae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7430649145:AAHrcGquqKQyj9t8rsu-MgNr6ybccVqHSe0")
