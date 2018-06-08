# vim:set ft=dockerfile:  
FROM drupalcomposer/selenium:base  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
ENV HUB_HOST hub  
ENV HUB_PORT 4444  
RUN apk --update --no-cache add \  
dbus \  
firefox \  
ttf-freefont \  
xvfb \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories \  
&& apk --update --no-cache add x11vnc  
  
RUN dbus-uuidgen > /var/lib/dbus/machine-id  
  
EXPOSE 5900  
COPY scripts/entrypoint.sh $SELENIUM_DIR  
ENTRYPOINT ["./entrypoint.sh"]  

