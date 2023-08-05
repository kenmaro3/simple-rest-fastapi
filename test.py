from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    user_id: str
    name: str
    group: str

app = FastAPI()

User_list =[
    {"user_id":"M001","name":"Takashi","group":"A"},
    {"user_id":"M002","name":"Hanako","group":"A"},
    {"user_id":"M003","name":"Hiroshi","group":"B"},
    {"user_id":"M004","name":"Kyoko","group":"B"},
    ]


#curl http://localhost:8000/Users/
@app.get("/Users/")
async def users():
    res = dict(users = User_list)
    return res


#curl http://localhost:8000/Users/{user_id}
@app.get("/Users/{uid}")
async def users(u_user_id:str):
    return list(filter(lambda item : item['user_id']==uid, User_list))


#curl -X POST -H "accept: application/json" -H "Content-Type: application/json" -d "{\"user_id\":\"M005\", \"Name\":\"Aya\", \"group\":\"C\"}," http://localhost:8000/Users/ 
@app.post("/Users/")
async def users(user: Item):
    User_list.append({"user_id": user.user_id,"name":user.name,"group":user.group})
    res = dict(users = User_list)
    return res
