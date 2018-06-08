FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
ENV REFRESHED_AT 2016-04-02-17-23  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get install -y software-properties-common && \  
apt-add-repository -y 'deb http://repo.pritunl.com/stable/apt trusty main' &&
\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv CF8E292A && \  
apt-get -y update && \  
apt-get install -y pritunl iptables ca-certificates && \  
/usr/lib/pritunl/bin/pip install --upgrade python-dateutil && \  
mkdir -p /var/log/pritunl  
  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 443  
EXPOSE 80  
EXPOSE 1194/udp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/pritunl", "start"]  

