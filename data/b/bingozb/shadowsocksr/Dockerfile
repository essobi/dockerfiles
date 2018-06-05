FROM alpine  
MAINTAINER bingo <bingov5@icloud.com>  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 12188  
ENV PASSWORD 01234567a  
ENV METHOD aes-256-cfb  
ENV PROTOCOL origin  
ENV PROTOCOLPARAM 32  
ENV OBFS plain  
ENV TIMEOUT 300  
ARG BRANCH=manyuser  
ARG WORK=~  
  
RUN apk --no-cache add python libsodium wget  
RUN mkdir -p $WORK && \  
wget -qO- --no-check-certificate
https://github.com/bingozb/shadowsocksr/archive/$BRANCH.tar.gz | tar -xzf - -C
$WORK  
  
WORKDIR $WORK/shadowsocksr-$BRANCH/shadowsocks  
  
EXPOSE $SERVER_PORT  
  
CMD python server.py \  
-s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k $PASSWORD \  
-m $METHOD \  
-O $PROTOCOL \  
-o $OBFS \  
-G $PROTOCOLPARAM \  
-t $TIMEOUT  

