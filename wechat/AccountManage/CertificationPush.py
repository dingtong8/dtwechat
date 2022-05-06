from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class Certification:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def certification_success(self):
        pass

    def certification_fail(self):
        pass

    def certification_name_success(self):
        pass

    def certification_name_fail(self):
        pass

    def year_careful_notice(self):
        pass

    def certification_expiration_notice(self):
        pass

