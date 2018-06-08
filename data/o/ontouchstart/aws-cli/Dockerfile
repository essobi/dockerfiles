FROM ubuntu:14.04.1  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ADD . /aws-cli  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -yq python-pip python-dev build-essential groff git  
RUN cd /aws-cli && pip install -r requirements.txt && pip install -e .  
  
ENV HOME /home  
WORKDIR /home  

