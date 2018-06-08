FROM alpine:latest  
  
MAINTAINER gael.mauleon@gmail.com  
  
RUN apk update && apk add squid && apk add sudo && rm -rf /var/cache/apk/*  
  
RUN echo "squid ALL=(ALL) NOPASSWD: /bin/chown -R squid\:squid /var/log/squid,
/bin/chown -R squid\:squid /var/cache/squid" >> /etc/sudoers.d/squid && \  
echo "Defaults:squid !requiretty" >> /etc/sudoers.d/squid && \  
chmod 440 /etc/sudoers.d/squid  
  
COPY squid.conf /etc/squid/squid.conf  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh  
  
EXPOSE 3128  
USER squid  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

