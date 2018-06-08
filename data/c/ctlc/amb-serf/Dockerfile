FROM ctlc/ambassador  
MAINTAINER lucas@rufy.com  
  
RUN apt-get install -qy unzip  
ADD https://dl.bintray.com/mitchellh/serf/0.5.0_linux_amd64.zip serf.zip  
RUN unzip serf.zip  
RUN rm serf.zip  
RUN mv serf /usr/bin/  
  
ADD /serf-join.sh /serf-join.sh  
ADD /start-socat.sh /start-socat.sh  
ADD /start-serf-service-registry.sh /start-serf-service-registry.sh  
ADD /supervisord-serf-service-registry.conf
/etc/supervisor/conf.d/supervisord-serf-service-registry.conf  
RUN chmod 755 /*.sh  
  
CMD ["/run.sh"]  

