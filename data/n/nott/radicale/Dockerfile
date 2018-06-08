FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y update; yum clean all;  
RUN yum -y install radicale  
  
ADD radicale.conf /etc/radicale/config  
ADD htpasswd /data/users  
RUN mkdir -p /data/collections && \  
chown -R radicale: /data/  
  
VOLUME ["/data/collections", "/var/log/radicale"]  
  
EXPOSE 5232  
  
USER radicale  
CMD /usr/bin/radicale -f  

