from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

#Define a basic route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/items/{item_id")
def read_item(item_id: int, q: str = None):
    return {"item_id":item_id, "query": q}