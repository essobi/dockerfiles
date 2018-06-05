## Dockerfile for Axiom  
## Mac Radigan  
FROM ubuntu:latest  
  
MAINTAINER Mac Radigan  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
## update APT  
RUN ulimit -n 1024  
RUN apt-get update --fix-missing  
  
## Axiom  
RUN apt-get update && \  
apt-get install -y \  
axiom \  
open-axiom \  
xterm  
  
# clean up APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Axiom entry point  
ADD ./axiom_ctl /usr/bin  
RUN chmod 775 /usr/bin/axiom_ctl  
ENTRYPOINT ["/usr/bin/axiom_ctl"]  
  
## *EOF*  

