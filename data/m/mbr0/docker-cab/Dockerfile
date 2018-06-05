FROM python:3-alpine  
LABEL Description="docker-cab image"  
MAINTAINER Marc Brinkmann <git@marcbrinkmann.de>  
  
COPY . /code  
WORKDIR /code  
RUN pip install .  
COPY ./templates /templates  
RUN rm -rf /code  
  
ENTRYPOINT ["/usr/local/bin/docker-cab"]  

