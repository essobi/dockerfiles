from python:alpine  
  
RUN apk update  
RUN apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-
dev  
RUN apk add --no-cache libpq  
COPY ./requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
RUN apk del deps  
RUN rm /requirements.txt  
  

