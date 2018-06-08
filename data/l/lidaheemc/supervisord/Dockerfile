# Docker image for supervisor on Ubuntu Linux.  
  
FROM ubuntu:xenial  
  
MAINTAINER Lida He, https://github.com/hldnova  
# Install software required for Elastalert  
RUN apt update && \  
apt install -y \--no-install-recommends \  
python-dev python-pip python-setuptools \  
curl less busybox && \  
  
# Install Supervisor.  
easy_install supervisor && \  
  
# Link command to busybox  
ln -s /bin/busybox /usr/bin/vi && \  
ln -s /bin/busybox /usr/bin/netstat && \  
ln -s /bin/busybox /usr/bin/ping && \  
ln -s /bin/busybox /usr/bin/ifconfig && \  
ln -s /bin/busybox /usr/bin/wget && \  
  
# Clean up.  
rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf ~/.cache &&
rm -rf /usr/share/doc  
  
ADD supervisord.conf /etc/supervisord.conf  
  
ENV TERM linux  
  
# default command  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

