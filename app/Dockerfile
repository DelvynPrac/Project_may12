ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install flask gunicorn


#USER appuser

COPY . . 

EXPOSE 4500

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:4500"]