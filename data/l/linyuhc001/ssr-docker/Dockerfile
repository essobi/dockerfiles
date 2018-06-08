FROM alpine:edge  
  
  
RUN apk update \  
&& apk add python libsodium unzip wget git \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /ssr \  
&& cd /ssr \  
&& git clone -b manyuser https://github.com/linyuhc001/shadowsocksr.git
/ssr/shadowsocks  
  
COPY config.json /config.json  
ADD dns.conf /ssr/shadowsocks/dns.conf  
ADD r.sh /ssr/shadowsocks/r.sh  
RUN chmod +x /ssr/shadowsocks/r.sh  
  
WORKDIR /ssr/shadowsocks  
  
CMD /ssr/shadowsocks/r.sh  

