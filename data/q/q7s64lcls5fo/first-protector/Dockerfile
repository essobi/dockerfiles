FROM ubuntu:16.04  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
RUN echo 'deb http://deb.torproject.org/torproject.org xenial main' >>
/etc/apt/sources.list.d/tor.list && \  
echo 'deb-src http://deb.torproject.org/torproject.org xenial main' >>
/etc/apt/sources.list.d/tor.list  
RUN gpg --keyserver keys.gnupg.net --recv
A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 && \  
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -  
RUN apt-get update && apt-get install -y tor deb.torproject.org-keyring jq
curl && \  
mkdir -p /var/data/tor && mkdir -p /etc/services.d/tor  
ADD torrc /etc/tor/torrc  
RUN tor --keygen --DataDirectory /var/data/tor && \  
tor --list-fingerprint --DataDirectory /var/data/tor --ORPort 443 --DirPort 80  
ADD tor-exit-notice.html /usr/share/tor-exit-notice.html  
ADD startup.sh /etc/cont-init.d/00_tor  
ADD tor.sh /etc/services.d/tor/run  
ENTRYPOINT ["/init"]

