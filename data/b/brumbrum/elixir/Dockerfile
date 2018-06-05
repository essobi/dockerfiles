FROM elixir:1.5-slim  
MAINTAINER Alessandro Lattao <me@alessandrolattao.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ=Europe/Rome  
  
# Update base image  
# Install software requirements  
RUN apt-get update && \  
apt-get -y --no-install-recommends install locales apt-utils && \  
echo "it_IT.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen it_IT.UTF-8 && \  
/usr/sbin/update-locale LANG=it_IT.UTF-8 && \  
apt-get -y upgrade && \  
apt-get -y --no-install-recommends install ca-certificates rsyslog zip unzip
awscli git zip unzip exiftool imagemagick webp && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  
  
ENV LC_ALL it_IT.UTF-8  
ENV LANGUAGE it_IT  
  
# Copio l'entrypoint.sh  
COPY bin/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
# Configuro rsyslog  
ADD etc/rsyslog.conf /etc/rsyslog.conf  
ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
  
# Define working directory.  
WORKDIR /data  
  
# Avvio  
ENTRYPOINT ["/entrypoint.sh"]  

