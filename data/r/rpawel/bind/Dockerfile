# runnable base  
FROM rpawel/ubuntu:trusty  
  
RUN apt-get -q -y update \  
&& apt-get dist-upgrade -y --no-install-recommends \  
# Install  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
bind9 dnsutils  
  
# Config  
ADD ./config /etc/  
RUN mkdir -p /var/log/supervisor \  
&& DEBIAN_FRONTEND=newt  
  
ADD build.sh /  
ADD run.sh /  
  
RUN chmod +x /build.sh /run.sh \  
&& bash /build.sh && rm -f /build.sh  
  
# PORTS  
EXPOSE 53/udp  
  
ENTRYPOINT ["/run.sh"]  

