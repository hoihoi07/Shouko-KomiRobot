"""
This Bot Was Developed By The Owner Of @jetbots.
Join his network and support him.
"""
import os
import dotenv


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  DOWNLOAD_LOCATION = "./@StrawHat_Network"
