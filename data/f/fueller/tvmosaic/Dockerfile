FROM debian:stretch  
MAINTAINER fueller  
  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y wget dbus dbus-x11 gconf2 supervisor htop nano procps lsof  
RUN wget -nv http://tv-mosaic.com/download/624e68fb8cfab4ce8d277d4a416af741 -O
tvmosaic.deb && \  
dpkg -i tvmosaic.deb && rm tvmosaic.deb  
  
RUN mkdir -p /var/log/supervisord  
RUN mkdir /var/run/dbus  
ADD /etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
ADD /etc/init.d/mosaic.sh /etc/init.d/mosaic.sh  
RUN chmod +x /etc/init.d/mosaic.sh  
  
RUN mkdir /opt-start && mv /usr/local/bin/tvmosaic /opt-start && mv
/opt/TVMosaic /opt-start  
  
VOLUME [ "/opt/TVMosaic", "/recordings", "/usr/local/bin/tvmosaic" ]  
EXPOSE 9270 9271  
ENTRYPOINT ["/usr/bin/supervisord"]  
CMD ["-c", "/etc/supervisor/conf.d/supervisord.conf"]  

