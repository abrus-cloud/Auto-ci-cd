# pull the official base image
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY req.txt /app

COPY . /app

WORKDIR /app


RUN pip install -r req.txt

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
