from django.db import models


class PublicChatRoom(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PublicChatMessage(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
