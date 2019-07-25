from environs import Env

env = Env()
env.read_env()

APP_SECRET = env.str("APP_SECRET")
MONGO_URI = env.str("MONGO_URI")
SEED_FILE = env.str("SEED_FILE")

class DsetCodeRule:
    def __init__(self):
        self.rules = None

    def save(self, rules):
        pass

    def _reload(self):
        pass