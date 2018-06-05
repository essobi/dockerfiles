# Dockerfile for haproxy  
# Version 1.0  
FROM ubuntu:14.04  
MAINTAINER Andre Christ <andre.christ@leanix.net>  
  
  
  
RUN apt-get update && apt-get install -y haproxy supervisor netcat  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/ambassador.conf  
  
ADD confd-0.7.1-linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
ADD haproxy.toml /etc/confd/conf.d/haproxy.toml  
ADD haproxy.cfg.tmpl /etc/confd/templates/haproxy.cfg.tmpl  
  
COPY rsyslog-haproxy.conf /etc/rsyslog.d/99-haproxy.conf  
COPY rsyslog-50-default.conf /etc/rsyslog.d/50-default.conf  
RUN rm -f /etc/rsyslog.d/haproxy.conf  
RUN sed -i 's/^#\$ModLoad imudp/\$ModLoad imudp/' /etc/rsyslog.conf  
RUN sed -i 's/^#\$UDPServerRun 514/\$UDPServerRun 514/' /etc/rsyslog.conf  
RUN sed -i 's/^\$ModLoad imklog.*/#\$ModLoad imklog/' /etc/rsyslog.conf  
RUN sed -i 's/^\$KLogPermitNonKernelFacility on/#\$KLogPermitNonKernelFacility
on/' /etc/rsyslog.conf  
  
CMD ["/usr/bin/supervisord"]  

