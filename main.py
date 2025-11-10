import os
import sys

import canvasapi
import dotenv
from canvasapi.exceptions import CanvasException


def main() -> None:
    """Entry point for retrieving Canvas user details."""

    dotenv.load_dotenv(dotenv.find_dotenv())

    token = os.environ.get("CANVAS_API_TOKEN")
    base_url = "https://ubc.instructure.com"

    if not token or not token.strip():
        print(
            "Missing CANVAS_API_TOKEN environment variable. "
            "Set it before running this script."
        )
        sys.exit(1)

    try:
        canvas_api = canvasapi.Canvas(base_url, token)
        result = canvas_api.get_user("self")
    except CanvasException as exc:
        print(f"Failed to authenticate with Canvas API: {exc}")
        sys.exit(1)

    print(result.attributes)


if __name__ == "__main__":
    main()
