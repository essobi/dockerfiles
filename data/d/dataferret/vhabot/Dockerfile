FROM ubuntu:trusty  
MAINTAINER Ted Chen <tedlchen@gmail.com>  
  
# Exposed Configuration Variables  
ENV LOGIN=""  
ENV PASS=""  
ENV ADMIN=""  
ENV VHABOT=""  
ENV DIMENSION="RubiKa"  
RUN \  
apt-get update && \  
apt-get install -y \  
bash nano wget unzip \  
mono-runtime libmono-corlib2.0-cil libmono-system-runtime2.0-cil mono-gmcs &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Change if older version no longer exists.  
ENV VHABOT_VERSION 0.7.13  
VOLUME /var/lib/vhabot  
  
RUN \  
wget
https://bitbucket.org/Llie/llie_vhabot/downloads/VhaBot_${VHABOT_VERSION}_LE_mono.zip
&& \  
unzip VhaBot_*_LE_mono.zip -d /opt && \  
rm VhaBot_*_LE_mono.zip && \  
ln -s /opt/VhaBot_${VHABOT_VERSION}_LE /opt/vhabot && \  
rm -rf /tmp/* /var/tmp/* && \  
useradd -u 999 vhabot && \  
chown vhabot.vhabot -R /opt/vhabot/data  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [""]  

