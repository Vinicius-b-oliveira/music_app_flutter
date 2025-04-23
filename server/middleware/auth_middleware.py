from fastapi import HTTPException, Header
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

password_key = os.getenv("PASSWORD_KEY")

def auth_middleware(x_auth_token = Header()): 
  try:
      if not x_auth_token:
        raise HTTPException(401, 'No auth token, acecess denied!')
      
      verified_token = jwt.decode(x_auth_token, password_key, algorithms=['HS256'])

      if not verified_token:
        raise HTTPException(401, 'Token verification failed, authorization denied')
      
      uid = verified_token.get('id')

      return {'uid': uid, 'token': x_auth_token}

  except jwt.PyJWTError:
    raise HTTPException(401, 'Token is not valid, authorization failed')