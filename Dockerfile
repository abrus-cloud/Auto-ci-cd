# pull the official base image
FROM python:3.10



RUN groupadd -g 1234 django && \
    useradd -m -u 1234 -g django django
USER django


ENV PYTHONPATH=/home/django/.local/bin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

COPY req.txt /app

COPY . /app



RUN pip install -r req.txt

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
