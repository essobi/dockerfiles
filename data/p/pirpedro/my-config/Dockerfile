#TO RUN docker run -d --name cmy-config my-config tail -f /dev/null  
# docker exec -it cmy-config /bin/bash  
FROM ubuntu:16.04  
MAINTAINER Pedro Rodrigues "pir.pedro@gmail.com"  
#Update aptitute  
RUN apt-get update  
  
ENV TERM dumb  
  
#Install software  
RUN apt-get install -y git  
  
#Create known hosts  
RUN mkdir -p $USER/.ssh  
RUN touch $USER/.ssh/known_hosts  
RUN ssh-keyscan github.com >> $USER/.ssh/known_hosts  
  
RUN mkdir -p /usr/local  
RUN git clone https://github.com/pirpedro/my-config.git /usr/local/my-config  

