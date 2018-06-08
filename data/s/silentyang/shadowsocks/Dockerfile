FROM debian:9  
ENV SSHOME=$HOME  
ENV SSMETHOD chacha20-ietf-poly1305  
ADD docker-entrypoint.sh /  
RUN chmod +x docker-entrypoint.sh \  
&& sh -c 'printf "deb http://deb.debian.org/debian stretch-backports main" >
/etc/apt/sources.list.d/stretch-backports.list' \  
&& apt-get update \  
&& apt-get install -y -t stretch-backports shadowsocks-libev  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 10000  

