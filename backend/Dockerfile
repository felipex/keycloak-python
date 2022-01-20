FROM python:3.9.7-alpine
#slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

# Install python and pip
RUN apk add bash
RUN apk add build-base libpq --no-cache --virtual .build-deps 
RUN pip install --upgrade pip

#RUN apk add --no-cache --update python3 py3-pip bash
ADD ./app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
#ADD ./app /opt/webapp/
WORKDIR /opt/webapp

# Expose is NOT supported by Heroku
EXPOSE 3000 		

# Run the image as a non-root user
RUN adduser -D negepe
USER negepe

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:3000 --reload wsgi:app

