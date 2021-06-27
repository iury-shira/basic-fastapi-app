from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:

    @staticmethod
    def bcrytp(pwd: str):
        return pwd_context.hash(pwd)
