FROM webhippie/php-caddy:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/storage", "/srv/www/vendor"]  
  
CMD ["/bin/s6-svscan", "/etc/s6"]  
EXPOSE 8080  
WORKDIR /srv/www  
  
ENV SOLDER_VERSION 0.7.3.1  
ENV SOLDER_TARBALL
https://github.com/TechnicPack/TechnicSolder/archive/v${SOLDER_VERSION}.tar.gz  
  
RUN apk update && \  
apk add \  
php7-apcu \  
sqlite && \  
rm -rf \  
/var/cache/apk/*  
  
RUN curl -sLo - \  
${SOLDER_TARBALL} | tar -xzf - --strip 1 -C /srv/www  
  
ADD rootfs /  

