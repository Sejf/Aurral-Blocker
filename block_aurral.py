from pynicotine.pluginsystem import BasePlugin


class Plugin(BasePlugin):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def init(self):
        self.log("Aurral Blocker Loaded")


    def disable(self):
        self.log("Aurral Blocker Unloaded")


    def upload_started_notification(self, user, file_path, *args):
        if user.startswith("aurral"):
            self._ban_user(user)


    def upload_queued_notification(self, user, file_path, *args):
        if user.startswith("aurral"):
            self._ban_user(user)


    def _ban_user(self, user):
        self.core.network_filter.ban_user(user)
        self.core.network_filter.ban_user_ip(user)
        self.log(f"User {user} was banned.")
