FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
  
WORKDIR /code  
  
RUN pip install --upgrade pip  
  
# Prevent polling that is killing Docker CPU when auto-reload is turned on  
RUN pip install pyinotify==0.9.6  
  
RUN apt-get install libmysqlclient-dev  
  
RUN pip install mysqlclient  
  
# Install python dependencies  
ADD requirements.txt /code/requirements.txt  
RUN pip install -r requirements.txt  
  
ADD . /code/  
  

