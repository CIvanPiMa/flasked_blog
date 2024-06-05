"""
This module is used to create the Post class and the FakePosts class.

- The Post class is used to represent a blog post.
- The FakePosts class is used to generate fake posts for the blog during development. It is a singleton class, meaning that only one instance of the class is created and shared across the application.

"""

import requests
from typing import Dict, Optional, Iterable

from flasked_blog.utils import SingletonMeta


class Post:
    """
    A class representing a blog post.

    Attributes
    ----------
    id : int
        The unique identifier of the post.
    title : str
        The title of the post.
    author : str
        The author of the post.
    date : str
        The date the post was published.
    body : str
        The main content of the post.
    subtitle : str
        The subtitle of the post.
    image_url : str
        The URL of the image associated with the post.

    Methods
    -------
    __str__() -> str
        Returns a string representation of the post.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        date: Optional[str] = None,
        body: Optional[str] = None,
        subtitle: Optional[str] = None,
        image_url: Optional[str] = None,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.date = date
        self.body = body
        self.subtitle = subtitle
        self.image_url = image_url

    def __str__(self):
        return f"{self.id}-{self.title}"


class FakePosts(metaclass=SingletonMeta):
    """
    A class used to generate fake posts for the blog.

    Attributes
    ----------
    posts : Dict[int, Post]
        A dictionary of posts where the key is the post identifier and the value is the Post object.
    
    Methods
    -------
    _generate_fake_posts()
        Generates fake posts for the blog.
    get_post_by_id(post_id: int) -> Post
        Returns a post given its identifier.
    get_all_posts() -> Iterable[Post]
        Returns all the posts.
    
    """
    def __init__(self):
        self.posts: Dict[int, Post] = None

    def _generate_fake_posts(self):
        """
        This method is used to generate fake posts for the blog.
        To modify the response, go to https://www.npoint.io/docs/5bf83aeb0f532e9e0fb7
        """
        if not self.posts:
            posts = requests.get("https://api.npoint.io/5bf83aeb0f532e9e0fb7")
            self.posts = {post["id"]: Post(**post) for post in posts.json()}

    def get_post_by_id(self, post_id: int) -> Post:
        if not self.posts:
            self._generate_fake_posts()
        return self.posts[post_id]

    def get_all_posts(self) -> Iterable[Post]:
        if not self.posts:
            self._generate_fake_posts()
        return list(self.posts.values())
