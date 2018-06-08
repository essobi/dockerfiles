FROM webhippie/php-caddy:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/srv/www/backups"]  
  
EXPOSE 8080  
WORKDIR /srv/www  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
RUN apk update && \  
apk add \  
mariadb-client \  
postgresql-client \  
sqlite && \  
rm -rf \  
/var/cache/apk/*  
  
ENV MYWEBSQL_VERSION master  
ENV MYWEBSQL_DOWNLOAD
https://github.com/Samnan/MyWebSQL/archive/${MYWEBSQL_VERSION}.tar.gz  
  
RUN curl -sLo - \  
${MYWEBSQL_DOWNLOAD} | tar -xzf - --strip 1 -C /srv/www  
  
ADD rootfs /  

