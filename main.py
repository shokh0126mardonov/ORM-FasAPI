import json

from app.db import initinal_db
from app.models import User,Post,Comment
from app.db import LocalSesion



initinal_db()

def insert_users()->None:
    db = LocalSesion()

    with open('demo/users.json') as jsonfile:
        data = json.load(jsonfile)

    for item in data:
        user = User(
            first_name = item['first_name'],
            last_name = item['last_name'],
            gender = item['gender'],
            username = item['username'],
            phone = item['phone']
        )

        db.bulk_save_objects([user])
        db.commit()

def insert_posts():
    db = LocalSesion()

    with open('demo/post.json',encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        posts = []
        for item in data:
            post = Post(
                title = item['title'],
                description = item['description'],
                user_id = item['user_id']
            )
            posts.append(post)

    db.bulk_save_objects(posts)
    db.commit()

def insert_comments()->None:

    db = LocalSesion()

    with open('demo/comments.json') as jsonfile:
        data = json.load(jsonfile)
        comments = []
        for item in data:
            comment = Comment(
                text = item['text'],
                user_id = item['user_id'],
                post_id = item['post_id'],
            )
            comments.append(comment)
    db.bulk_save_objects(comments)
    db.commit()
