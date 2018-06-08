# Dockerfile for syncthing  
FROM xamindar/archlinux-base:2015-05-13  
MAINTAINER xamindar <junkxamindar@gmail.com>  
  
# Environment variables  
ENV HOME /home  
ENV QUASSEL_CONFIG /config  
ENV QUASSEL_USER nobody  
ENV LISTEN 0.0.0.0  
ENV SSL_COUNTRY US  
ENV SSL_STATE State  
ENV SSL_LOCATION City  
ENV SSL_ORG Company  
ENV SSL_GROUP Section  
ENV SSL_NAME unRaid  
ENV SSL_EMAIL unraid@unraid.org  
  
  
# Copy additional files to container  
# install.sh script  
COPY install.sh /tmp/  
# Custom supervisord.conf file for docker container  
COPY supervisord.conf /etc/  
# create ssl certificate and start quassel scripts.  
COPY create-cert.sh /home/  
COPY create-cert.conf /etc/supervisor.d/  
# quassel-core program launch file for supervisor  
COPY quassel-core.conf /etc/supervisor.d/  
# Run Install script  
RUN chmod +x /home/*  
RUN chmod +x /tmp/install.sh && /bin/bash /tmp/install.sh && rm
/tmp/install.sh  
  
# Volumes  
# Map /config to host defined config path (/mnt/user/appdata/syncthing)  
VOLUME /config  
  
# Ports in use by this application.  
EXPOSE 4242  
# run supervisor  
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

