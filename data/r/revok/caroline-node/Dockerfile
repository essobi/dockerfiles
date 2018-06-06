FROM revok/base:latest  
MAINTAINER "Arun Neelicattu" <arun.neelicattu@gmail.com>  
  
USER root  
RUN yum -y install libnotify hostname  
USER ${REVOK_USER}  
ADD assets/supervisord.conf /etc/supervisord.conf  
ADD assets/revok.conf ${REVOK_CONF}/revok.conf  
ADD assets/revok-caroline-start ${REVOK_HOME}/bin/revok-caroline-start  
  
RUN mkdir ${REVOK_HOME}/report  
  
VOLUME ["${REVOK_HOME}/report"]  
  
CMD ["/usr/bin/supervisord", "-n"]  

