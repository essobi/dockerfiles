FROM webhippie/php-caddy:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/piwik", "/srv/www/vendor"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
EXPOSE 8080  
WORKDIR /srv/www  
  
ENV PIWIK_VERSION 3.2.0  
ENV PIWIK_TARBALL http://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz  
ENV GEOIP_TARBALL
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz  
  
ENV CRON_ENABLED true  
  
RUN apk update && \  
apk add \  
git \  
php7-ldap && \  
rm -rf \  
/var/cache/apk/*  
  
RUN curl --create-dirs -sLo /srv/www/misc/GeoIPCity.dat.gz ${GEOIP_TARBALL} &&
\  
gunzip /srv/www/misc/GeoIPCity.dat.gz  
  
RUN curl -sLo - ${PIWIK_TARBALL} | tar -xzf - --strip 1 -C /srv/www && \  
chown -R caddy:caddy /srv/www  
  
ADD rootfs /  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/piwik.git"  
LABEL org.label-schema.name="Piwik"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

