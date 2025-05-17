from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import subprocess
import os

app = FastAPI()

@app.post("/run")
async def run_hedra_script(
    aspect_ratio: str = Form(...),
    resolution: str = Form(...),
    text_prompt: str = Form(...),
    audio_file: UploadFile = Form(...),
    image: UploadFile = Form(...)
):
    # Save uploaded files
    audio_path = "input_audio.mp3"
    image_path = "input_image.png"

    with open(audio_path, "wb") as f:
        f.write(await audio_file.read())
    with open(image_path, "wb") as f:
        f.write(await image.read())

    command = [
        "uv", "run", "main.py",
        "--aspect_ratio", aspect_ratio,
        "--resolution", resolution,
        "--text_prompt", text_prompt,
        "--audio_file", audio_path,
        "--image", image_path
    ]

    try:
        subprocess.run(command, check=True)
        return JSONResponse({"status": "success", "message": "Video generation started."})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
