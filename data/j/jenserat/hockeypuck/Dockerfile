FROM ubuntu:14.04  
MAINTAINER Jens Erat <email@jenserat.de>  
  
# Prevent daemon start during install  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl  
  
# Install and setup PostgreSQL  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
&& \  
apt-add-repository ppa:hockeypuck/ppa && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y hockeypuck && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 11370 11371  
VOLUME /etc/hockeypuck  
VOLUME /var/lib/hockeypuck/recon-ptree/  
USER hockeypuck  
CMD ["/usr/bin/hockeypuck", "run", "--config",
"/etc/hockeypuck/hockeypuck.conf"]  

