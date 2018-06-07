FROM debian:jessie-slim  
MAINTAINER Extra <extra84@gmail.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
lsb-release \  
&& apt-get remove -y \  
&& rm -rf /var/cache/apt/archives/*  
  
COPY murmur.ini /etc/murmur.tpl  
COPY murmur.x86 /usr/bin/murmur  
COPY init.sh /usr/bin/init.sh  
  
RUN useradd -u 9000 murmur \  
&& mkdir -p /data \  
&& chown murmur.murmur /data \  
&& chmod +r /etc/murmur.tpl  
  
VOLUME ["/data"]  
EXPOSE 64738 64738/udp  
  
CMD ["/usr/bin/init.sh"]  
  

