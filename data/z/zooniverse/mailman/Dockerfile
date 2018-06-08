FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
lighttpd \  
mailman \  
rsyslog \  
supervisor \  
postfix-policyd-spf-python \  
opendkim \  
opendkim-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser postfix opendkim  
  
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY logrotate.conf /etc/logrotate.d/mailman  
COPY start.sh /usr/local/bin/start.sh  
COPY rsyslog-hup.sh /etc/cron.daily/zzz-rsylog-hup  
COPY mailman-restart.sh /etc/cron.hourly/mailman-restart  
  
RUN chmod +x /usr/local/bin/start.sh  
  
EXPOSE 25 80  
ENTRYPOINT [ "/usr/local/bin/start.sh" ]  

