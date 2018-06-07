FROM centos:7  
MAINTAINER Elvin Tan <elvin@elvin.net>  
RUN yum -y install epel-release && yum -y update  
RUN yum -y install lm_sensors rrdtool rrdtool-perl  
COPY rrd-sensor-cron.pl /rrd-sensor-cron.pl  
VOLUME ["/data"]  
ENTRYPOINT ["/rrd-sensor-cron.pl"]  
# docker run -d --name=rrd-sensor -v /opt/rrd-sensor:/data visago/rrd-sensor  

