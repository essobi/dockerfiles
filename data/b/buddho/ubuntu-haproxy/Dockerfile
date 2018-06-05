#  
# HAProxy Dockerfile  
#  
# http://github.com/buddho-io/docker-ubuntu-haproxy  
  
FROM ubuntu:14.04  
MAINTAINER lance@buddho.io  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update the system  
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf
/var/lib/apt/lists/*  
# Add APT backports and install HAProxy  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y curl haproxy=1.5.3-1~ubuntu14.04.1 && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \  
rm -rf /var/lib/apt/lists/*  
# Install Confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.6.3/confd-0.6.3-linux-
amd64 -o /usr/local/sbin/confd && \  
chmod 755 /usr/local/sbin/confd  
  
ADD etc/confd/conf.d /etc/confd/conf.d  
  
ADD usr/local/sbin/confd-watch.sh /usr/local/sbin/confd-watch  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
EXPOSE 22002  
# Define working directory.  
RUN mkdir -p /var/lib/haproxy && chown -R haproxy:haproxy /var/lib/haproxy  
WORKDIR /var/lib/haproxy  
  
CMD /usr/local/sbin/confd-watch  

