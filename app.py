from fastapi import FastAPI, UploadFile
from face_swap import face_swap
app = FastAPI()


@app.post("/face-swap")
async def create_upload_file(avatar: UploadFile):
  file_location = f"uploads/{avatar.filename}"
  with open(file_location, "wb+") as file_object:
      file_object.write(avatar.file.read())
  new_file_location = face_swap(file_location)
  return {"path": new_file_location}