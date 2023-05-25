import json

from autotraders import AutoTradersSession


class SpaceTradersEntity:
    def __init__(self, session: AutoTradersSession, update, action_url):
        self.session: AutoTradersSession = session
        self.action_url = session.base_url + action_url  # TODO: Better get() and post() methods
        if self.action_url[-1] != "/":
            self.action_url += "/"
        if update:
            self.update()

    def get(self, action: str = None) -> dict:
        if action is None:
            r = self.session.get(self.action_url[0 : len(self.action_url) - 1]) # noqa E203
        else:
            r = self.session.get(
                self.action_url + action,
            )
        j = r.json()
        if "error" in j:
            raise IOError(j["error"]["message"])
        return j

    def post(self, action: str, data=None) -> dict:
        self.session.headers["Content-Type"] = "application/json"
        if data is not None:
            r = self.session.post(
                self.action_url + action,
                data=json.dumps(data),
            )
        else:
            r = self.session.post(self.action_url + action)
        j = r.json()
        if "error" in j:
            raise IOError(j["error"]["message"])
        return j

    def update(self):
        pass
