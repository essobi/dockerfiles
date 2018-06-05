FROM alpine:3.4  
MAINTAINER Michael Kenney <mkenney@webbedlam.com>  
  
ENV NLS_LANG American_America.AL32UTF8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV TIMEZONE America/Denver  
  
COPY ./container/.my.cnf /root/.my.cnf  
  
RUN set -x \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add \  
curl \  
mysql-client \  
shadow \  
&& apk del \  
curl \  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/mysql"]  

