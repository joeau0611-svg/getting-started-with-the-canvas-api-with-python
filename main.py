"""Minimal connectivity check for the Canvas API."""

import os

import dotenv
from canvasapi import Canvas

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get("CANVAS_API_TOKEN")
BASE_URL = os.environ.get("CANVAS_BASE_URL", "https://ubc.instructure.com")

if not TOKEN:
    raise SystemExit("Set CANVAS_API_TOKEN in your environment or .env file before running main.py")

canvas_api = Canvas(BASE_URL, TOKEN)
result = canvas_api.get_user("self")
print(result.attributes)
