FROM ubuntu:trusty  
  
# Remove red warning text  
ENV DEBIAN_FRONTEND "noninteractive"  
# install deluge  
RUN apt-get update -q && \  
apt-get install -qy software-properties-common && \  
add-apt-repository ppa:deluge-team/ppa && \  
apt-get update -q && \  
apt-get install -qy deluged deluge-console deluge-web  
  
# allow multiverse and install unrar  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security multiverse" >>
/etc/apt/sources.list && \  
# echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security-updates
multiverse" >> /etc/apt/sources.list && \  
apt-get -qy update && \  
apt-get -qy install unrar unzip  
# kanske även behöver zip och par2?  
#RUN apt-get install -qy nano  
# mount volumes for config and downloads  
VOLUME ["/config", "/torrents"]  
  
# add starrt script  
ADD start.sh /start.sh  
  
# daemon port  
EXPOSE 58846  
#webui port  
EXPOSE 8112  
# incoming torrents  
EXPOSE 58946  
EXPOSE 58946/udp  
  
# change UMask  
#RUN echo "umask 007" >> /root/.profile  
# run with init.d for umask  
RUN echo -e '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d  
ADD deluge-daemon /etc/init.d/  
ADD deluge-daemon_user /etc/default/  
RUN chmod 755 /etc/init.d/deluge-daemon  
RUN update-rc.d deluge-daemon defaults  
  
# runs start script when starting  
CMD ["/start.sh"]  

