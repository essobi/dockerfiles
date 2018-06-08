# vim: set filetype=dockerfile  
FROM limed/ubuntu-base:14.04  
MAINTAINER limed@sudoers.org  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN apt-get -q update && \  
apt-get install -qy --force-yes python-cheetah \  
python-openssl \  
git \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
# Create app and data directory  
RUN mkdir -p /app && \  
mkdir -p /data/sickbeard && \  
mkdir -p /data/sabnzbd && \  
git clone https://github.com/midgetspy/Sick-Beard.git /app  
  
# App dir is for apps, and /data is where config and database will live  
VOLUME /app  
VOLUME /data/sickbeard  
VOLUME /data/sabnzbd  
  
COPY files/supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 8081  
CMD [ "/usr/bin/supervisord" ]  

