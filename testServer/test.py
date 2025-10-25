from fastapi import FastAPI, Depends, WebSocket, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import User, Deck
from schemas import UserCreate, UserOut, DeckOut
from auth import create_user, authenticate_user
from websocket import manager

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.post("/login", response_model=UserOut)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user

@app.get("/decks", response_model=list[DeckOut])
def get_decks(user_id: int, db: Session = Depends(get_db)):
    return db.query(Deck).filter(Deck.owner_id == user_id).all()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message: {data}")
    except:
        manager.disconnect(websocket)
