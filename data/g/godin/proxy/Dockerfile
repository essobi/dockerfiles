FROM ubuntu:14.04  
RUN apt-get update \  
&& useradd -u 1000 docker-proxy \  
&& apt-get -y install squid3 \  
&& mv /etc/squid3/squid.conf /etc/squid3/squid.conf.default \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY squid.conf /etc/squid3/squid.conf  
  
VOLUME /var/spool/squid3  
  
COPY docker-entrypoint.sh /  
RUN chmod +x ./docker-entrypoint.sh  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

