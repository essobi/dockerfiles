FROM ubuntu:wily  
MAINTAINER falms <F@L.fal.ms>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y sarg && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /log  
VOLUME ["/log"]  
ENTRYPOINT ["sarg", "-o", "/log/sarg-reports/"]  

