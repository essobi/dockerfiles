FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
ENV REFRESHED_AT 2016-04-06-18-20  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:adiscon/v8-stable && \  
apt-get -y update && \  
apt-get install -y rsyslog rsyslog-elasticsearch python-pip cron logrotate &&
\  
pip install supervisor && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
mkdir -p /var/log/containers && mkdir -p /rsyslog  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY rsyslog.conf /etc/rsyslog.conf  
COPY logrotate.conf /etc/logrotate.conf  
  
RUN (crontab -l 2>/dev/null; echo "*/5 * * * * /usr/sbin/logrotate
/etc/logrotate.conf") | crontab -  
  
VOLUME ["/var/log", "/var/spool/rsyslog"]  
  
EXPOSE 514  
ENTRYPOINT ["supervisord"]  
CMD ["-c", "/etc/supervisord.conf"]  

