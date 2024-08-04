# pull the official base image
FROM python:3.10


USER python

# set work directory
WORKDIR /home/python

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY --chown=python:python req.txt /app
RUN pip install -r req.txt

# copy project
COPY --chown=python:python . /home/python


#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
