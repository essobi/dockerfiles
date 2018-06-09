FROM ubuntu:14.04  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update  
RUN apt-get install -yq python-pip wget awscli  
RUN pip install --quiet boto==2.35.2 project-runpy==0.3.1 Delorean==0.4.5  
  
ADD src /app/  
WORKDIR /app  

