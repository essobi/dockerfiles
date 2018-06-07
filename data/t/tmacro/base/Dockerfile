FROM alpine:latest  
MAINTAINER Taylor McKinnon <mail@tmacs.space>  
  
ENV S6_VERSION 1.11.0.1  
# add apk_add convienence script  
ADD ./apk_add /usr/bin/  
RUN chmod +x /usr/bin/apk_add  
  
# Install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-
amd64.tar.gz  
  
CMD ["/init"]

