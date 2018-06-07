FROM alpine:3.5  
MAINTAINER Shoma Nishitateno <shoma416@gmail.com>  
  
RUN set -ex \  
&& apk update \  
&& apk add --no-cache \  
dumb-init \  
rsyslog \  
dovecot=2.2.27-r0  
  
RUN set -ex \  
&& addgroup -S vdovecot -g 1000 \  
&& adduser -D -S -h /dev/null -s /sbin/nologin -G vdovecot vdovecot -u 1000  
  
ADD files/* /etc/dovecot/conf.d/  
ADD docker-entrypoint.sh /  
  
EXPOSE 110 143  
ENTRYPOINT ["/bin/sh"]  
  
CMD ["/docker-entrypoint.sh"]  

