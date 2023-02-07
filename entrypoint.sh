#!/bin/bash

echo "Running migrations"
python -m alembic revision --autogenerate -m "add basic user table"
python -m alembic upgrade head

echo "Running app"
python -m uvicorn shop.main:app --host 0.0.0.0 --port 8001 --reload