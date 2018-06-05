FROM ubuntu:12.04  
MAINTAINER tym  
  
RUN apt-get update  
RUN apt-get install -y privoxy squid python-pip nginx  
RUN pip install shadowsocks  
  
ENV SERVER_ADDR your.server.address  
ENV PORT 30000  
ENV PASSWORD password  
ENV CACHE_SIZE 256  
ADD domestic /home/domestic  
ADD good-sites /home/good-sites  
  
# configure privoxy  
RUN cat /etc/privoxy/config | sed '/^listen-address */c listen-address
0.0.0.0:8118' | sed '/#\s*forward-socks5\s/c forward-socks5 \/ localhost:1080
.' > config  
  
# configure squid3  
RUN cat /etc/squid3/squid.conf | sed -n '/^[a-zA-z0-9]/p' | sed '/^acl/d' |
sed '/^http_access */d' | sed '/^http_port */c http_port 3128' | sed
'/^refresh_pattern (/c refresh_pattern
\\\\.(jpg|png|gif|mp3|xml|html|htm|css|js) 1440 50% 2880 ignore-reload' >
squid.conf  
RUN echo "http_access allow all" >> squid.conf  
RUN echo "cache_peer 127.0.0.1 parent 8118 0 no-query" >> squid.conf  
RUN echo "prefer_direct on" >> squid.conf  
RUN echo "forwarded_for transparent" >> squid.conf  
RUN echo "acl domestic dst \"/home/domestic\"" >> squid.conf  
RUN echo "acl good_sites dstdomain \"/home/good-sites\"" >> squid.conf  
RUN echo "always_direct allow domestic" >> squid.conf  
RUN echo "never_direct allow good_sites" >> squid.conf  
# RUN echo "always_direct allow all" >> squid.conf  
RUN echo "cache_mem $CACHE_SIZE MB" >> squid.conf  
RUN echo "cache_access_log /var/log/squid3/access.log" >> squid.conf  
RUN echo "cache_log /var/log/squid3/cache.log" >> squid.conf  
RUN echo "cache_store_log /var/log/squid3/store.log" >> squid.conf  
  
RUN mv config /etc/privoxy/config  
RUN mv squid.conf /etc/squid3/squid.conf  
  
EXPOSE 3128  
EXPOSE 80  
CMD ["sh", "-c", \  
"printenv | grep 80_TCP.*PORT | awk -F'=' '{print $2}' >
/usr/share/nginx/www/index.html && service nginx start && \  
service privoxy restart && squid3 && sslocal -s $SERVER_ADDR -p $PORT -k
$PASSWORD -l 1080 -t 600 -m aes-256-cfb"]  

