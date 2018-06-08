FROM python:3-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev  
  
COPY requirements.txt /usr/src/app/  
  
RUN pip3 install --no-cache-dir -r requirements.txt  

