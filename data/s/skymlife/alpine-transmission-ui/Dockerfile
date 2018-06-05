FROM alpine:3.6  
MAINTAINER Sergey Savchenko <skymlife@yandex.ru>  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk add --update transmission-daemon ca-certificates openssl tzdata wget && \  
update-ca-certificates && rm -rf /var/cache/apk/* && \  
cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime  
  
ADD ./start.sh /start.sh  
ADD ./settings.example.json /settings.example.json  
ADD ./settings.example.json /config/settings.json  
ADD ./tr-control-easy-install.sh /tr-control-easy-install.sh  
  
RUN chmod u+x /start.sh && mkdir -p /downloads /watch /config /incomplete && \  
sh tr-control-easy-install.sh  
  
VOLUME ["/downloads", "/incomplete", "/watch", "/config"]  
  
EXPOSE 9091 45555  
CMD ["/start.sh"]  

