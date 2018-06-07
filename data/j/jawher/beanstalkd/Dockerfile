FROM debian:jessie  
  
MAINTAINER jawher  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# update apt  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y beanstalkd && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/data"]  
  
EXPOSE 11300  
CMD ["/usr/bin/beanstalkd", "-f", "60000", "-b", "/data"]

