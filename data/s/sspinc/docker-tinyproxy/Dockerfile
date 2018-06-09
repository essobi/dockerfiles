# Tinyproxy (https://banu.com/tinyproxy/)  
FROM ubuntu:trusty  
MAINTAINER Ryan Seto <ryanseto@yak.net>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install tinyproxy && \  
rm -rf /var/lib/apt/lists/*  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN install -vdo nobody -g nogroup -m 0755 /var/run/tinyproxy  
  
# Configure Tinyproxy  
# This allows allows all connections.  
RUN sed -i -e"s/^Allow /#Allow /" /etc/tinyproxy.conf  
  
USER nobody  
EXPOSE 8888  
CMD ["/usr/sbin/tinyproxy", "-d"]  

