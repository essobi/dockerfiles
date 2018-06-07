FROM python:3.6.0-alpine  
  
LABEL authors="Chad Crawford, Jason Bennefield"  
LABEL version="0.1"  
LABEL description="Manages WPEngine installations for our website."  
  
ADD ./app/requirements.txt /app/requirements.txt  
RUN apk add --update alpine-sdk openssl-dev libffi-dev python3-dev &&\  
pip install -r /app/requirements.txt &&\  
apk del alpine-sdk  
  
VOLUME ["/app/volume"]  
  
## Add the entrypoint script  
ADD ./app /app  
RUN chmod 777 /app/entrypoint.py  
  
## Add the Wordpress template files  
ADD wp-template /app/wp-template  
  
## Set the working directory to our app directory  
WORKDIR /app  

