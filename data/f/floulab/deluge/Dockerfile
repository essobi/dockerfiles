FROM ubuntu:xenial  
MAINTAINER Ioannis Angelakopoulos <ioagel@gmail.com>  
  
ENV DELUGE_USER media  
ENV DELUGE_USER_UID 10000  
ENV DELUGE_GROUP media  
ENV DELUGE_GROUP_UID 10000  
ENV DELUGE_HOME /var/lib/deluge  
  
#install deluge  
RUN apt update && \  
apt install -qy tzdata && \  
apt install -qy supervisor && \  
apt install -qy software-properties-common && \  
apt install -qy python-software-properties && \  
add-apt-repository -y ppa:deluge-team/ppa && \  
apt update && \  
apt install -qy deluged deluge-web && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /supervisord.conf  
  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh && \  
rm -f /etc/localtime  
  
VOLUME $DELUGE_HOME  
  
# torrent port  
EXPOSE 55100  
EXPOSE 55100/udp  
# daemon port  
EXPOSE 58846  
# WebUI  
EXPOSE 8112  
CMD ["start.sh"]  

