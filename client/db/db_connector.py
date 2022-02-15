import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from client.db.models import UserData
from client import config


class DB:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(f"sqlite:///{config.DB_PATH}")
        UserData.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

    def update_user_data(
            self,
            token: str,
            login: str,
            password: str,
            # name: str,
            # surname: str
    ) -> None:
        self.session.add(
            UserData(
                token=token,
                login=login,
                password=password,
                # name=name,
                # surname=surname
            )
        )
        self.session.commit()

    def update_token(self, token: str):
        self.session.query(UserData).first().token = token
        self.session.commit()

    def delete_data(self) -> None:
        self.session.query(UserData).delete()
        self.session.commit()

    def get_token(self) -> str:
        row = self.session.query(UserData).first()
        if row is not None:
            return row.token
        return ""


db = DB()

if __name__ == "__main__":
    db.delete_data()
    print("data deleted")
