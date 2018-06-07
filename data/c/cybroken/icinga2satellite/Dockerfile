FROM phusion/baseimage  
MAINTAINER Werner Glanzer <wernerglanzer@googlemail.com>  
  
RUN apt-get update  
RUN apt-get -y install wget supervisor nagios-plugins  
  
# Install Icinga2  
RUN wget -O - http://packages.icinga.org/icinga.key | apt-key add - && \  
echo 'deb http://packages.icinga.org/ubuntu icinga-trusty main' >
/etc/apt/sources.list.d/icinga-main-trusty.list \  
apt-get update && apt-get install -y icinga2  
  
# Configure supervisor  
RUN mkdir /opt/supervisor  
COPY config/supervisor/icinga2.conf /etc/supervisor/conf.d/icinga2.conf  
COPY config/supervisor/icinga2_supervisor /opt/supervisor/icinga2_supervisor  
  
# Configure Icinga2 satellite  
RUN mv /etc/icinga2/conf.d /etc/icinga2/conf.d_orig  
COPY config/icinga /etc/icinga2/conf.d  
COPY config/start.sh /opt/start.sh  
CMD ["/opt/start.sh"]  

