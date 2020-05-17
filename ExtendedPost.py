from BasePost import BasePost
import time

class ExtendedPost(BasePost):
    def __init__(self, userId, id, title, body):
        super().__init__(userId, id, title, body)
        self.createdAt = time.asctime(time.localtime(time.time()))

