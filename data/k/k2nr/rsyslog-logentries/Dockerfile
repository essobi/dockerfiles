FROM debian:jessie  
  
EXPOSE 514/tcp 514/udp  
VOLUME ["/var/log", "/etc/rsyslog.d"]  
  
RUN apt-get update && \  
apt-get install -q -y rsyslog-gnutls ruby && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./run.sh /bin/run.sh  
COPY ./rsyslog.conf /etc/rsyslog.conf  
  
COPY ./logentries.all.crt /etc/ssl/certs/logentries.all.crt  
COPY ./logentries.conf.erb /etc/rsyslog.d/logentries.conf.erb  
  
ENTRYPOINT [ "/bin/run.sh", "-n" ]  

