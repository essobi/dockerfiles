FROM ubuntu:latest  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install deluged deluge-web supervisor && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m -s /bin/sh user && \  
passwd -d user  
  
EXPOSE 8112 58846  
VOLUME /config /data  
  
ADD start.sh /  
ADD services.conf /etc/supervisor/conf.d/  
  
CMD ["/start.sh"]  

