# Docker image
FROM python:3.7-alpine 

# Who maintains the file
MAINTAINER Subhrokanti

# Run python with unbuffered mode
ENV PYTHONUNBUFFERED 1

# Store requirements from local requirements.txt to docker's requirement.txt
COPY ./requirements.txt /requirements.txt

# Install dependencies related to POSTGRES
RUN apk add --update --no-cache postgresql-client 

# Install temporary dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

# Install requirements on docker file
RUN pip3 install -r /requirements.txt

# Delete temp deps
RUN apk del .tmp-build-deps

# Make directory in docker image to store application source code
RUN mkdir /app

# Switch to that directory
WORKDIR /app

# Copy local code to docker image
COPY ./app /app

# Create and switch to that user
# This will run docker image as a user and not as a root
RUN adduser -D user
USER user