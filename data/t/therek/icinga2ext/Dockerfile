# Dockerfile for icinga2 with icingaweb2  
# https://github.com/therek/docker-icinga2ext  
  
FROM jordan/icinga2:2.8.0  
MAINTAINER Cezary Morga <cm@therek.net>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libnet-snmp-perl \  
dnsutils \  
whois \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80 443 5665  
  
ENTRYPOINT ["/opt/run"]  

