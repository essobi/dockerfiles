FROM debian:jessie  
  
MAINTAINER Niklas Wilcke <wilcke@cybus.io>  
  
EXPOSE 53  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" | tee
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -t jessie-backports -q -y pdns-server pdns-backend-remote \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm /etc/powerdns/pdns.d/*  
  
############################################  
# Command to install PowerDNS 4.0.0 (alpha?)  
############################################  
#  
# RUN apt-get update \  
# && DEBIAN_FRONTEND=noninteractive apt-get install -y curl apt-transport-
https \  
# && curl -sL https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - \  
# && echo "deb https://repo.powerdns.com/debian jessie-auth-40 main" | tee
/etc/apt/sources.list.d/powerdns.list \  
# && echo "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600"
> /etc/apt/preferences.d/pdns \  
# && apt-get update \  
# && DEBIAN_FRONTEND=noninteractive apt-get install -y pdns-server pdns-
backend-remote \  
# && DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove curl apt-
transport-https  
  
CMD ["/usr/sbin/pdns_server", "--daemon=no", "--guardian=no"]  

