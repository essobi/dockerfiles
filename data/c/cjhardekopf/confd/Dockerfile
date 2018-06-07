FROM ubuntu:trusty  
MAINTAINER Chris Hardekopf <cjh@ygdrasill.com>  
  
# Update and install supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
# Get and install confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.6.3/confd-0.6.3-linux-
amd64 /tmp/  
RUN mv /tmp/confd-0.6.3-linux-amd64 /opt/confd && \  
chmod a+x /opt/confd && \  
mkdir -p /etc/confd/{conf.d,templates}  
  
# Add the start script  
ADD start /opt/  
  
CMD [ "/opt/start" ]  

