FROM gliderlabs/alpine:3.4  
MAINTAINER maran@bytesized-hosting.com  
  
ENV HOME="/root"  
RUN apk add --no-cache --virtual=build-dependencies curl tar bash tzdata # s6
s6-portable-utils  
RUN apk add --no-cache --repository
http://nl.alpinelinux.org/alpine/edge/community shadow  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz /  
RUN tar -xvf /s6-overlay-amd64.tar.gz  
  
RUN mkdir -p /config /media /data  
  
RUN useradd -U -d /config -s /bin/false bytesized  
  
RUN rm -rf /var/cache/apk/* /tmp/* /s6-overlay-amd64.tar.gz  
ADD /static /  
  
ENTRYPOINT ["/init"]  

