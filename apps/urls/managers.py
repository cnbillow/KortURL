"""
*  Author:   Vincent Yim
*  FileName: managers.py
*  Software: PyCharm
*  Blog:     https://yandenghong.github.io
"""
from django.db import models
from apps.utils.transfer_url import code_generator


class LinkMapManager(models.Manager):

    def get_or_create_map(self, user, url, expire_time=None):
        code = code_generator.get_code()
        while self.filter(code=code).exists():
            code = code_generator.get_code()
        data = dict()
        data["user"] = user
        data["url"] = url
        data["code"] = code
        if expire_time:
            data["expire_time"] = expire_time
        return self.get_or_create(raw_url=url, created_by=user, defaults=data)



