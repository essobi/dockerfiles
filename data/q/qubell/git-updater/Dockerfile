FROM ubuntu:latest  
MAINTAINER Roman Timushev <rtimushev@qubell.com>  
  
RUN apt-get install -y git  
  
ENV GIT_BRANCH master  
  
ADD git-updater /usr/local/bin/  
  
VOLUME /source  
WORKDIR /source  
  
ENTRYPOINT /usr/local/bin/git-updater  

