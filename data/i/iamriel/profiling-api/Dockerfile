FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
MAINTAINER Riel  
  
RUN apt-get update && \  
apt-get install -y && \  
mkdir /code && \  
mkdir /srv/logs  
  
WORKDIR /code  
ADD . /code/  
  
RUN pip install -r requirements/base.txt  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

