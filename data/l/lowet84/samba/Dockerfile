FROM phusion/baseimage  
  
RUN apt-get update && \  
apt-get install -y samba && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN (echo gurkburk; echo gurkburk) | smbpasswd -a root -s  
ADD start.sh /start.sh  
CMD sh start.sh  

