from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from src.core.config import Config
from fastapi.security.api_key import APIKeyHeader

SECRET_KEY = Config.SECRET_KEY
ALGORITHM = Config.ALGORITHM
API_KEY = Config.API_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=True)

def verify_token(token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_aud": False})
        return payload  # Puedes extraer datos del token aquí
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
            raise HTTPException(status_code=403, detail="API Key inválida")
    return api_key
