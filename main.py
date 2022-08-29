from Lightning import LightningAPI
import uvicorn
from flask_sqlalchemy import SQLAlchemy





app = LightningAPI()

users = {
    "user1":{
        "frist_name":"Ari",
        "last_name":"Bermeki",
        "birth_date":"20.01.1996",
        "nationality":"Deutschland",
    },
     "user2":{
        "frist_name":"Karin",
        "last_name":"Knutsson",
        "birth_date":"20.01.1996",
        "nationality":"Schweden",
    },
     "user3":{
        "frist_name":"Jaafar",
        "last_name":"Bermeki",
        "birth_date":"20.01.1996",
        "nationality":"Deutschland",
    }
}


@app.get('/')
async def home():
    return users["user2"]
# @app.post('/')
# async def home():
#     return users["user1"]


