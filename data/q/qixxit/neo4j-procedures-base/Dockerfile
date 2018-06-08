FROM openjdk:8u141-jdk  
MAINTAINER Leif Gensert <leif@leif.io>  
  
ENV PATH="/root/.local/bin:${PATH}"  
RUN apt-get update  
RUN apt-get install -y python-pip  
RUN pip install awscli --upgrade

