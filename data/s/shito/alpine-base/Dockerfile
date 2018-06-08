FROM alpine:edge  
MAINTAINER Sebastian Faujour <sf@bytepark.de>  
  
WORKDIR /tmp  
  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
bash \  
gosu \  
&& rm -rf /var/cache/apk/*  
  
COPY /rootfs /  
  
COPY ./files/init.sh /init.sh  
RUN chmod +x /init.sh  
  
ENTRYPOINT ["/init.sh"]

