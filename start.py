import os
import uvicorn

uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
