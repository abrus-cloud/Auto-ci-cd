# pull the official base image
FROM python:3.10


USER www-data

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY --chown=www-data:www-data req.txt /app
RUN pip install -r req.txt

# copy project
COPY --chown=www-data:www-data . /app


#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
