FROM ubuntu:16.04  
MAINTAINER Óscar de Arriba <odarriba@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install transmission  
RUN apt-get update && \  
apt-get dist-upgrade -y -qq && \  
apt-get install transmission-daemon -y -qq && \  
apt-get clean && \  
rm -rf /tmp/*  
  
# Create directories and so on  
RUN mv /var/lib/transmission-daemon/info /config && \  
ln -s /config /var/lib/transmission-daemon/info && \  
mkdir /config_original && \  
sed -i '/USER=debian_transmission/c\USER=root' /etc/init.d/transmission-daemon
&&\  
mkdir -p /downloads  
  
COPY config/settings.json /config_original/settings.json  
COPY start_service.sh /start_service.sh  
  
VOLUME ["/downloads", "/config"]  
  
EXPOSE 9091 51413/tcp 51413/udp  
  
CMD ["/bin/bash", "/start_service.sh"]

