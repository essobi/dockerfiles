FROM debian:jessie  
  
LABEL maintainer="Chopin Ngo <consatan@gmail.com>" \  
github="https://github.com/consatan/docker_tor_clientonly" \  
description="Starts Tor project on `ClientOnly` mode and exposes a SOCKS port
for client use."  
  
ENV TOR_VERSION 0.2.9.10*  
  
RUN set -ex \  
&& echo "deb http://deb.torproject.org/torproject.org jessie main" >>
/etc/apt/sources.list \  
&& echo "deb-src http://deb.torproject.org/torproject.org jessie main" >>
/etc/apt/sources.list \  
&& gpg \--keyserver keys.gnupg.net --recv
A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 \  
&& gpg \--export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends tor=${TOR_VERSION}
deb.torproject.org-keyring \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# config torrc  
&& echo "Log notice stdout" >> /etc/tor/torrc \  
&& echo "SocksPort 0.0.0.0:9050" >> /etc/tor/torrc \  
&& echo "ClientOnly 1" >> /etc/tor/torrc  
  
EXPOSE 9050  
  
ENTRYPOINT ["/usr/bin/tor", "-f /etc/tor/torrc"]  

