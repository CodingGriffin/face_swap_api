from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/result_uploads", StaticFiles(directory="result_uploads"), name="static")
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from face_swap import face_swap


@app.post("/face-swap")
async def create_upload_file(avatar: UploadFile):
  file_location = f"uploads/{avatar.filename}"
  with open(file_location, "wb+") as file_object:
      file_object.write(avatar.file.read())
  new_file_location = face_swap(file_location)
  return {"result": new_file_location}