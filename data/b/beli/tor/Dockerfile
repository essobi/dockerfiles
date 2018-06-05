FROM debian:stretch  
MAINTAINER Michal Belica <devel@beli.sk>  
EXPOSE 9050  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
gnupg dirmngr \  
&& apt-key adv --keyserver ipv4.pool.sks-keyservers.net --recv
A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 \  
&& echo 'deb http://deb.torproject.org/torproject.org stretch main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
tor tor-geoipdb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
COPY torrc /etc/tor/  
RUN mv /var/lib/tor / && ln -s /tor /var/lib/  
VOLUME /tor  
CMD ["/usr/bin/tor"]  

