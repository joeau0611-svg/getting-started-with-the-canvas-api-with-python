import os
import sys

import dotenv
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException

dotenv.load_dotenv(dotenv.find_dotenv())

token = os.environ.get("CANVAS_API_TOKEN")
base_url = "https://ubc.instructure.com"

if not token or not token.strip():
    sys.exit(
        "Missing CANVAS_API_TOKEN environment variable. "
        "Set it before running this script."
    )

try:
    canvas_api = Canvas(base_url, token)
    result = canvas_api.get_user("self")
except CanvasException as exc:
    sys.exit(f"Failed to authenticate with Canvas API: {exc}")

print(result.attributes)
