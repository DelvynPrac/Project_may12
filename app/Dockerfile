ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install -r requirements.txt.1.3


USER appuser

COPY . . 

EXPOSE 8000

CMD ["python3", "-m" "guvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]