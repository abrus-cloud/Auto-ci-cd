# pull the official base image
FROM python:3.10


RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python
USER python

# set work directory
WORKDIR /home/python

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY req.txt /app
RUN pip install -r req.txt

# copy project
COPY . /home/python


#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
