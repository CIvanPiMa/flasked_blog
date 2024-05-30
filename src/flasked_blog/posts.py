import requests
from typing import List


class Post:
    def __init__(self, id: int = None, title: str = None, body: str = None, subtitle: str = None, image_url: str = None):
        self.id = id
        self.title = title
        self.body = body
        self.subtitle = subtitle
        self.image_url = image_url
        self._fake_posts: List["Post"] = []

    def __str__(self):
        return f"{self.id}-{self.title}"

    def _generate_fake_posts(self) -> List["Post"]:
        if not self._fake_posts:
            posts = requests.get("https://api.npoint.io/5bf83aeb0f532e9e0fb7")
            self._fake_posts = [Post(**post) for post in posts.json()]
        return self._fake_posts
