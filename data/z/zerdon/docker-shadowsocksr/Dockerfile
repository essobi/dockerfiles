# Dockerfile for shadowsocksr  
FROM alpine:3.5  
MAINTAINER zerdon <zerdon1991@gmail.com>  
  
ENV SSR_SERVER_PORT 8080  
ENV SSR_PASSWORD password  
ENV SSR_METHOD chacha20  
ENV SSR_PROTOCOL auth_aes128_md5  
ENV SSR_OBFS http_simple  
  
RUN apk update && \  
apk --no-cache upgrade && \  
apk --no-cache add libsodium git python && \  
cd ~ && \  
git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git  
  
EXPOSE $SSR_SERVER_PORT  
  
CMD python /root/shadowsocksr/shadowsocks/server.py -p $SSR_SERVER_PORT -k
$SSR_PASSWORD -m $SSR_METHOD -O $SSR_PROTOCOL -o $SSR_OBFS  

