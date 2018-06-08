FROM ubuntu:14.04  
MAINTAINER Marco Salafia <marco.salafia@gmail.com>  
  
RUN apt-get update && apt-get install -y python-pip  
RUN pip install mkdocs  
RUN mkdir docs  
  
WORKDIR /docs  
VOLUME /docs  
EXPOSE 8000  

