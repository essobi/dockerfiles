FROM ubuntu:trusty  
MAINTAINER anderson@infraops.info  
  
ENV BIND_USER=bind \  
BIND_VERSION=1:9.9.5 \  
WEBMIN_VERSION=1.8 \  
DATA_DIR=/data \  
DHCP_ENABLED=true \  
INTERFACES= \  
WEBMIN_ENABLED=true  
  
RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \  
&& apt-get update \  
&& apt-get install -y rsyslog supervisor nano vim zsh wget dnsutils lnav \  
&& wget http://www.webmin.com/jcameron-key.asc -qO - | apt-key add - \  
&& echo "deb http://download.webmin.com/download/repository sarge contrib" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y bind9=${BIND_VERSION}*
bind9-host=${BIND_VERSION}* webmin=${WEBMIN_VERSION}* isc-dhcp-server \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY dhcpd.conf.exemple /etc/dhcp/dhcpd.conf  
COPY supervisord.conf /etc/supervisord.conf  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
RUN touch /var/log/syslog  
RUN chown syslog:adm /var/log/syslog  
  
VOLUME ["${DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

