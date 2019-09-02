import peewee

db = peewee.SqliteDatabase('app.db')
db.connect()


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    chat_id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField()


class Activity(BaseModel):
    user = peewee.ForeignKeyField(model=User)
    message = peewee.TextField()


if __name__ == "__main__":
    db.create_tables([User, Activity])
