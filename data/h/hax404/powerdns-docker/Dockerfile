FROM debian:jessie  
MAINTAINER Georg Haas <hax404foogit@hax404.de>  
  
#ENV LANG en_US.UTF-8  
#ENV LC_ALL en_US.UTF-8  
ENV LANG C  
#ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
VOLUME "/data"  
  
RUN \  
echo "Acquire::Languages \" none\";\nAPT::Install-Recommends
\"true\";\nAPT::Install-Suggests \"false\";" > /etc/apt/apt.conf ;\  
echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure tzdata ;\  
apt-get -q -y update ;\  
apt-get install -y pdns-recursor pdns-server pdns-backend-mysql pdns-backend-
sqlite3 ;\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
CMD ["/usr/local/bin/entrypoint.sh"]  
  
EXPOSE 53/udp 53/tcp  
  

