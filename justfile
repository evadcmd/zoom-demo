dev:
    uv run uvicorn zoom_demo.main:api --reload --app-dir src
test:
    uv run pytest --cov -s
