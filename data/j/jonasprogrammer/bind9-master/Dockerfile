FROM debian:stretch  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install --no-install-recommends -y bind9 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mv /etc/bind/named.conf.local /etc/bind/named.conf.local-dist \  
&& ln -s /data/zones.conf /etc/bind/named.conf.local  
  
ENV DOMAINS=example.com,example.org TTL=86400  
EXPOSE 53 53/udp  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

