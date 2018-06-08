from debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y \  
postfix \  
postfix-mysql \  
rsyslog \  
sasl2-bin \  
sendemail \  
supervisor \  
&& apt-get -y clean \  
&& apt-get -y purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
add install.sh /opt/install.sh  
expose 25  
cmd /opt/install.sh; /opt/postfix.sh  
#/usr/bin/supervisord -c /etc/supervisor/supervisord.conf

