FROM ubuntu:16.04  
# add xenial tor repository  
RUN echo 'deb http://deb.torproject.org/torproject.org xenial main' >
/etc/apt/sources.list.d/tor.list && \  
gpg --keyserver keys.gnupg.net --recv 886DDD89 && \  
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -  
  
# install tor  
RUN apt-get update && apt-get -y install --no-install-recommends \  
tor \  
deb.torproject.org-keyring \  
&& rm -rf /var/lib/apt/lists/* && apt-get -y clean  
  
RUN echo "User debian-tor\nDataDirectory /var/lib/tor\nSocksPort 0.0.0.0:9050"
> /etc/tor/torrc  
  
VOLUME /var/lib/tor  
VOLUME /etc/tor/  
  
EXPOSE 9050  
CMD ["/usr/bin/tor", "-f", "/etc/tor/torrc"]  

