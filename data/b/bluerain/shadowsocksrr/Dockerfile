FROM alpine:3.7  
ENV SERVER_ADDR=0.0.0.0 \  
SERVER_PORT=80 \  
PASSWORD=sample123 \  
METHOD=none \  
PROTOCOL=auth_chain_f \  
OBFS=http_simple  
  
  
ARG BRANCH=akkariiin/dev  
  
  
RUN apk --no-cache add python libsodium wget && \  
wget --no-check-certificate
https://github.com/shadowsocksrr/shadowsocksr/archive/"$BRANCH".zip \  
-O ssrr.zip && mkdir ssrr && unzip ssrr.zip -d ssrr && mv ssrr/*/* ssrr/ && rm ssrr.zip && \  
apk del wget  
  
WORKDIR /ssrr  
  
EXPOSE $SERVER_PORT  
CMD python shadowsocks/server.py -m $METHOD -s $SERVER_ADDR -p $SERVER_PORT -k
$PASSWORD -o $OBFS -O $PROTOCOL  

