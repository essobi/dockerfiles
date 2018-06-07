FROM debian:jessie  
MAINTAINER Chris Staley me@unixtime.site  
  
RUN apt-get update && apt-get upgrade -y && apt-get install git -y  
RUN apt-get -y clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run.sh /run.sh  
  
VOLUME ["/repo", "/root/.ssh"]  
  
CMD ["/bin/bash", "/run.sh"]

