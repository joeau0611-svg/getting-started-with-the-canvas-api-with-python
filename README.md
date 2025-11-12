# Getting Started with the Canvas API with Python

This project now includes an end-to-end course builder that provisions the
WorldEd Tutor & Coordinator Training experience in Canvas.  The helper script
uses the Canvas API to create assignment groups, pages, assignments, quizzes,
discussions, and modules that match the narrative and structure described in
the build guide.

## Getting Started
These instructions will get you a copy of the script up and running on your local machine for use with Canvas and your own API tokens. This script makes a request to the Canvas API that displays basic information about your user profile.

### Prerequisites

1. **Install [Python 3.7 or greater](https://www.python.org/downloads/)**.
2. **Install [Git](https://git-scm.com/downloads)**.

### Installation

*Not sure how to clone a repo? Check out this [helpful guide first!](https://codeburst.io/git-and-github-in-a-nutshell-b0a3cc06458f)*

1. Open command prompt on Mac or command line on Windows.
2. Clone this repo. `git clone https://github.com/ubccapico/getting-started-with-the-canvas-api-with-python.git`
3. Then cd into the repo. `cd getting-started-with-the-canvas-api-with-python`
4. Install dependencies. `pip install -r requirements.txt` (If you see `bash: pip: command not found`, try using `pip3 install -r requirements.txt`).

### Configure Canvas access

Generate a Canvas API token from the account that owns (or has permission to
edit) the target course.  Create a `.env` file based on `sample.env` and set:

```
CANVAS_BASE_URL=https://yourinstitution.instructure.com
CANVAS_API_TOKEN=your_token_here
CANVAS_COURSE_ID=12345
```

You can also provide these values on the command line when running the builder.

### Provision the course

Run the course builder to create or update all resources:

```
python build_course.py
```

You can target a specific course ID or Canvas instance without the `.env` file:

```
python build_course.py 12345 --base-url https://yourinstitution.instructure.com --token your_token_here
```

The script is idempotent—you can re-run it to refresh copy, quiz questions, and
module structure without creating duplicates.

### Optional: profile check

`main.py` remains as a minimal example that prints the authenticated user
profile.  This is useful for verifying connectivity:

```
python main.py
```

### Tips

The API connects to your production Canvas instance.  If you prefer to use the
Beta or Test environment, update the base URL (for example,
`https://ubc.test.instructure.com`) and generate a token from that environment.

## Authors

* **Justin Lee**
https://github.com/justin0022 | justin.lee@ubc.ca
* **Andrew Gardener**
https://github.com/andrew-gardener | andrew.gardener@ubc.ca

## License

This project is licensed under the GPL 3 License.
