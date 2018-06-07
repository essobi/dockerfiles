FROM webhippie/php-caddy:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/storage", "/srv/www/vendor"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
EXPOSE 8080  
WORKDIR /srv/www  
  
ENV INVOICENINJA_VERSION 2.5.0.3  
ENV INVOICENINJA_TARBALL
https://github.com/invoiceninja/invoiceninja/archive/v${INVOICENINJA_VERSION}.tar.gz  
  
RUN apk update && \  
apk add \  
git \  
php-apcu \  
sqlite&& \  
rm -rf \  
/var/cache/apk/*  
  
RUN curl -sLo - \  
${INVOICENINJA_TARBALL} | tar -xzf - --strip 1 -C /srv/www  
  
ADD rootfs /  

