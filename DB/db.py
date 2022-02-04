import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from DB.models import UserData


class DB:
    def __init__(self):
        self.engine = sqlalchemy.create_engine("sqlite:///sqlite3.db")
        UserData.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

    def update_user_data(
            self,
            id: int,
            token: str,
            login: str,
            password: str,
            name: str,
            surname: str) -> None:
        self.session.add(
            UserData(
                id=id,
                token=token,
                login=login,
                password=password,
                name=name,
                surname=surname
            )
        )
        self.session.commit()

    def update_token(self, token: str):
        self.session.query(UserData).first().token = token
        self.session.commit()

    def delete_data(self) -> None:
        self.session.query(UserData).delete()
        self.session.commit()


if __name__ == "__main__":
    db = DB()
    db.update_user_data(12, "sdf", "sdf", "sdf", "sdf", "sdf")
    db.update_token("qwe")