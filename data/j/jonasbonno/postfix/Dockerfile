FROM debian:stretch-slim  
  
MAINTAINER Jonas Bonno Mikkelsen (https://github.com/JonasBonno)  
  
RUN apt-get update && apt-get -y --no-install-recommends install \  
ca-certificates \  
postfix \  
rsyslog && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY rsyslog.conf /etc/rsyslog.conf  
COPY run /root/run  
RUN chmod +x /root/run  
  
VOLUME ["/var/lib/postfix", "/var/mail", "/var/spool/postfix"]  
EXPOSE 25  
CMD ["/root/run"]  

