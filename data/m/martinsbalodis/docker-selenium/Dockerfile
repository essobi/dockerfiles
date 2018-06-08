FROM ubuntu:xenial  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DISPLAY :1  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install wget openjdk-8-jre-headless xfonts-100dpi xfonts-75dpi \  
xfonts-scalable xfonts-cyrillic tightvncserver supervisor expect \  
firefox fonts-ipafont-gothic xfonts-scalable && \  
mkdir /opt/selenium && \  
wget http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar -O /opt/selenium/selenium-server-standalone.jar && \  
expect -c 'set timeout 3;spawn /usr/bin/vncpasswd;expect "*?assword:*";send --
"selenium\r";expect "*?erify:*";send -- "selenium\r";expect "*?view-only
password*";send -- "n\r";send -- "\r";expect eof' && \  
apt-get remove -y --purge wget expect && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/*  
  
# vnc server startup script  
ADD start-vncserver.sh /start-vncserver.sh  
  
# Supervisor Config  
ADD supervisor-conf.d /etc/supervisor/conf.d  
  
# Expose Ports  
EXPOSE 4444 5901  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

