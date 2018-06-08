FROM haproxy:1.5  
MAINTAINER kim@conduct.no  
  
RUN apt-get update && apt-get install -y openssl --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
WORKDIR /etc/ssl  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
COPY run.sh /usr/local/etc/haproxy/run.sh  
VOLUME ["/etc/ssl"]  
CMD ["/usr/local/etc/haproxy/run.sh"]  

