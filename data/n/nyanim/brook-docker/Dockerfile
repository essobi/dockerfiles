FROM alpine:latest  
  
LABEL maintainer "Frank <i@nyan.im>"  
  
ARG VER=v20180227  
ARG URL=https://github.com/txthinking/brook/releases/download/$VER/brook  
  
ARG PASS=brookpass  
  
ADD $URL /usr/bin/  
  
RUN set -ex && \  
chmod +x /usr/bin/brook  
  
EXPOSE 9999  
CMD brook -l :9999 -p $PASS

