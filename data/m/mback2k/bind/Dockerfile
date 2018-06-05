FROM mback2k/debian:stretch  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
dnsutils && \  
apt-get install -y --no-install-recommends \  
bind9 bind9utils && \  
apt-get clean  
  
EXPOSE 53/tcp 53/udp  
  
VOLUME /etc/bind  
VOLUME /var/cache/bind  
  
ADD docker-entrypoint.d/ /run/docker-entrypoint.d/  
  
CMD ["/usr/sbin/named", "-f", "-u", "bind"]  

