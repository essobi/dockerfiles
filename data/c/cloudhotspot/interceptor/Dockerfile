FROM alpine  
MAINTAINER Justin Menga <justin.menga@cloudhotspot.co>  
  
RUN echo "http://nl.alpinelinux.org/alpine/edge/main/" >>
/etc/apk/repositories && \  
apk update && \  
apk add --no-cache bash squid ca-certificates openssl tcpdump curl  
  
COPY files/* /etc/squid/  
  
RUN /usr/lib/squid/ssl_crtd -c -s /var/lib/ssl_db -M 16MB && \  
chown -R squid:squid /var/lib/ssl_db/ && \  
ln -sf /dev/stdout /var/log/squid/access.log  
  
# Set entrypoint and default command arguments  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["squid","-f","/etc/squid/squid.conf","-NYCd","1"]

