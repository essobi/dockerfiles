FROM alpine:3.2  
MAINTAINER SHS <shs@overstack.ru>  
  
ENV GOMAXPROCS 2  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && apk upgrade && \  
apk add curl bash jq tar gzip ca-certificates consul && \  
curl -s -L https://dl.bintray.com/mitchellh/consul/0.5.2_web_ui.zip -o
/tmp/ui.zip && \  
curl -s -L https://github.com/sequenceiq/docker-alpine-
dig/releases/download/v9.10.2/dig.tgz|tar -xzv -C /usr/local/bin/ && \  
cd /tmp && unzip ui.zip && mv dist /ui &&\  
rm -rf /var/cache/apk/* /usr/local/src/* /tmp/*  
  
COPY ./config /config  
COPY ./docker-entrypoint.sh /  
  
VOLUME /data  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp 53/udp  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["consul"]  

