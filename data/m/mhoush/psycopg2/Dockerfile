FROM python:alpine  
  
RUN apk update  
RUN apk add --virtual deps \  
gcc \  
python-dev \  
linux-headers \  
musl-dev \  
postgresql-dev  
  
RUN apk add --no-cache \  
libpq \  
make  
  
RUN pip install --upgrade pip \  
psycopg2  
  
VOLUME /app  

