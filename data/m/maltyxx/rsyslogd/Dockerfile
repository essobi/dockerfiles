FROM debian:jessie  
  
MAINTAINER Yoann VANITOU <yvanitou@gmail.com>  
  
ENV RSYSLOG_VERSION 8.4.2  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install rsyslog="$RSYSLOG_VERSION*"
&& \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 514/tcp 514/udp  
  
VOLUME ["/var/log"]  
  
COPY ./etc/rsyslog.conf /etc/rsyslog.conf  
COPY ./etc/rsyslog.d/30-docker.conf /etc/rsyslog.d/30-docker.conf  
COPY ./etc/logrotate.d/docker-logs /etc/logrotate.d/docker-logs  
  
CMD ["rsyslogd", "-n"]  

