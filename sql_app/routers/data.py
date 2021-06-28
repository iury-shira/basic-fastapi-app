from fastapi import APIRouter, Depends
from .. import schemas, oauth2

router = APIRouter(
    prefix='/data',
    tags=['Data']
)


@router.get("/")
def read_data(current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return {"message": f'Acesso permitido para {current_user.username.split()[0]}'}
