FROM webhippie/php-caddy:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/kanboard"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
EXPOSE 8080  
WORKDIR /srv/www  
  
RUN apk update && \  
apk upgrade && \  
apk add \  
git \  
sqlite \  
php7-ldap && \  
rm -rf \  
/var/cache/apk/*  
  
ENV KANBOARD_VERSION 1.2.2  
ENV KANBOARD_TARBALL
https://github.com/kanboard/kanboard/archive/v${KANBOARD_VERSION}.tar.gz  
  
RUN curl -sLo - \  
${KANBOARD_TARBALL} | tar -xzf - --strip 1 -C /srv/www && \  
chown -R caddy:caddy /srv/www  
  
ADD rootfs /  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/kanboard.git"  
LABEL org.label-schema.name="Kanboard"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

