from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:

    @staticmethod
    def bcrytp(pwd: str):
        return pwd_context.hash(pwd)

    @staticmethod
    def match_pwd(plain_pwd: str, hashed_pwd: str):
        return pwd_context.verify(plain_pwd, hashed_pwd)
