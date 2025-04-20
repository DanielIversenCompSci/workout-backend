from fastapi import FastAPI, HTTPException

# run w uvicorn main:app --reload
app = FastAPI()

arms_routine = ["monday", "tuesday", "wednesday", "thursday", "friday"]

# Root
@app.get("/")
def read_root():
    return {"message": "Hello, macOS FastAPI dev!"}


####################
# Arms Routine
####################

# HTTP GET
@app.get("/arms-routine/{session_id}")
def get_session_by_id(session_id: int):
    if session_id < len(arms_routine):
        return arms_routine[session_id]
    else:
        raise HTTPException(status_code=404, detail="Session not found")


# HTTP POST
@app.post("/arms-routine")
def create_arms_routine(session: str):
    arms_routine.append(session)
    return arms_routine

