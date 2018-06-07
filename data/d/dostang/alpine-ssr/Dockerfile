FROM alpine:3.5  
RUN apk --no-cache add python libsodium unzip openssl ca-certificates \  
&& update-ca-certificates  
  
RUN cd / \  
&& wget https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O
/tmp/manyuser.zip \  
&& unzip -d /tmp /tmp/manyuser.zip \  
&& mv /tmp/shadowsocksr-manyuser/shadowsocks / \  
&& rm -rf /tmp/*  
  
ADD dns.conf /shadowsocks/dns.conf  
ADD config.json /shadowsocks/config.json  

