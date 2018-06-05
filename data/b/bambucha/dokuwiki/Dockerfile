FROM alpine:3.5  
MAINTAINER Dmitry Prazdnichnov <dp@bambucha.org>  
  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=https://github.com/bambocher/docker-dokuwiki \  
org.label-schema.license=MIT \  
org.label-schema.schema-version=1.0  
  
RUN apk --no-cache add lighttpd php5-cgi php5-curl php5-gd php5-json \  
php5-openssl php5-xml php5-zlib curl tar \  
&& curl -sL
https://github.com/splitbrain/dokuwiki/archive/release_stable_$VERSION.tar.gz
\  
| tar xz -C /srv --strip-components=1 \  
&& chown -R lighttpd. /srv \  
&& apk del curl tar \  
&& sed -ie "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/php.ini  
  
COPY lighttpd.conf /etc/lighttpd/  
  
USER lighttpd  
VOLUME ["/srv/data", "/srv/lib/plugins", "/srv/conf", "/srv/lib/tpl"]  
EXPOSE 8080  
ENTRYPOINT ["lighttpd"]  
CMD ["-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

