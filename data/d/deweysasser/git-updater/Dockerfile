FROM debian:jessie  
MAINTAINER Dewey Sasser <dewey@sasser.com>  
# Purpose: Periodically update a path  
RUN apt-get update  
RUN apt-get -y install git gnupg rsync wget  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.1/dumb-init_1.0.1_amd64 && chmod +x
/usr/local/bin/dumb-init  
  
ADD run.sh /run.sh  
ADD root /root  
  
# How long to sleep between checks  
ENV SLEEP 300  
# false to skip signature check. anything else to require signature  
# all files in /keys will be importing to gpg to check signatures  
ENV SIGNED false  
  
# Place to copy the git files if signature checks  
ENV TARGET /volume  
  
# Location for the GPG import keys  
ENV KEYS /keys  
  
ENTRYPOINT [ "dumb-init", "/run.sh" ]  

