FROM ubuntu:zesty  
  
MAINTAINER Mike Ortiz <mike@jellydice.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y supervisor && \  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/bin/supervisord", "-n"]  

