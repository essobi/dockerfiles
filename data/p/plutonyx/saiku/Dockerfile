FROM ubuntu:latest  
  
MAINTAINER Zulu Ng <ngz1357@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
vim \  
less \  
default-jdk  
  
RUN wget -P /usr/local http://meteorite.bi/downloads/saiku-latest.zip  
RUN unzip -u /usr/local/saiku-latest.zip -d /usr/local  
  
RUN rm /usr/local/saiku-latest.zip  
EXPOSE 8080  
CMD /usr/local/saiku-server/start-saiku.sh && tail -f /usr/local/saiku-
server/tomcat/logs/catalina.out

