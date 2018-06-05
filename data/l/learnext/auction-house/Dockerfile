FROM python:3.6.2-jessie  
  
COPY requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
  
RUN mkdir /code  
COPY . /code  
  
WORKDIR /code  

