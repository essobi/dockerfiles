FROM debian:stretch  
  
RUN \  
apt-get update && \  
apt-get install -y systemd rsyslog && \  
rm -rf /var/lib/apt/lists/*  
  
COPY bin/logrotate.sh /usr/bin/logrotate.sh  
COPY bin/entrypoint.sh /usr/bin/entrypoint.sh  
COPY etc/rsyslog.conf /etc/journald-to-syslog/rsyslog.conf  
COPY etc/logrotate.conf /etc/journald-to-syslog/logrotate.conf  
  
CMD /usr/bin/entrypoint.sh  

