FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
RUN mkdir -p /code  
WORKDIR /code  
  
ADD ./cash_machine /code  
  
RUN apt-get update && \  
apt-get install -y python-psycopg2  
  
RUN pip install -r requirements.txt  

