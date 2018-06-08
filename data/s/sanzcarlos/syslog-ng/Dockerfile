# Version: 3.8.2  
FROM debian:stable-slim  
  
MAINTAINER Carlos Sanz <carlos.sanzpenas@gmail.com>  
  
LABEL org.label-schema.vendor = "Personal" \  
org.label-schema.name = "Syslog-NG" \  
org.label-schema.version = "3.8-stable" \  
org.label-schema.version = "latest" \  
org.label-schema.docker.cmd = "docker run -p 514:514 sanzcarlos/syslog-ng" \  
org.label-schema.name = "Syslog-NG" \  
org.label-schema.build-date = "2018-01-08"  
  
RUN apt-get update -qq && \  
apt-get dist-upgrade -y -qq && \  
apt-get install -y syslog-ng && \  
apt-get autoremove -y -qq && \  
apt-get autoclean -y -qq && \  
rm -rf /var/lib/apt/lists/*  
  
ADD https://raw.githubusercontent.com/sanzcarlos/syslog-ng/master/syslog-
ng/stable/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
  
EXPOSE 514/udp  
EXPOSE 601/tcp  
# EXPOSE 6514/tcp  
ENTRYPOINT ["/usr/sbin/syslog-ng", "-F"]  

