FROM ubuntu:16.04  
MAINTAINER Jaekwon Park <jaekwon.park@code-post.com>  
  
ENV VERSION squid-3.5.27  
WORKDIR /usr/local/squid  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends make ca-certificates gcc iptables curl build-essential
aptitude libssl-dev openssl libgnutls-dev && \  
aptitude build-dep squid -y .&& apt-get clean && rm -rf /var/lib/apt/lists/*
&& \  
curl http://www.squid-cache.org/Versions/v3/3.5/squid-3.5.27.tar.gz -o
/tmp/squid-3.5.27.tar.gz && \  
tar -xzvf /tmp/squid-3.5.27.tar.gz -C /usr/local/ && rm
/tmp/squid-3.5.27.tar.gz && \  
cd /usr/local/squid-3.5.27 && ./configure --with-openssl --enable-async-io
--enable-icmp --enable-htpc --enable-ssl-crtd --with-gnutls --with-openssl &&
\  
make && make install && make install clean && apt-get purge -y -q --auto-
remove make ca-certificates gcc aptitude libssl-dev libgnutls-dev && rm -rf
/usr/local/squid-3.5.27  
  
EXPOSE 3128 3129  
VOLUME /etc/squid/  
  
ADD ./entrypoint.sh /  
RUN chmod 0755 /entrypoint.sh  
CMD ["/entrypoint.sh"]  

