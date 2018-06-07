  
FROM debian:jessie  
  
MAINTAINER Rafa Couto <caligari@treboada.net>  
  
VOLUME ["/var/spool/mail/"]  
  
EXPOSE 25  
RUN echo "$HOSTNAME" > /etc/hostname \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
supervisor \  
rsyslog \  
postfix \  
mailutils \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf \  
&& sed -i 's/\/dev\/xconsole/\/dev\/stdout/' /etc/rsyslog.conf  
  
ENV HOSTNAME="mail" \  
DOMAIN="example.com" \  
MY_NETWORKS="127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128"  
CMD ["/usr/bin/python", "/usr/bin/supervisord", "--
configuration=/opt/supervisor/supervisord.conf"]  
  
ADD opt /opt  
  

