from fastapi import FastAPI
from app.routes import items,suppliers,users
from app.db.database import Base,engine



# Create DataBase
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(suppliers.router, prefix="/suppliers", tags=["Suppliers"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Stock Control Management System"}
