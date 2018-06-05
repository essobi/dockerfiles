FROM debian:testing  
MAINTAINER Michal Belica <devel@beli.sk>  
EXPOSE 8333  
EXPOSE 8332  
# app runs as user bitcoin(1000) inside the container  
# add unstable repo and set pins  
RUN echo "deb http://ftp.us.debian.org/debian unstable main" >>
/etc/apt/sources.list \  
&& echo "Package: *\nPin: release a=unstable\nPin-Priority: 800" >>
/etc/apt/preferences  
  
# grab gosu for easy step-down from root  
RUN apt-get update && apt-get install -y --no-install-recommends gnupg dirmngr
ca-certificates wget \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove ca-certificates wget gnupg dirmngr \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends bitcoind \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
COPY bitcoin.conf /etc/  
COPY entrypoint /  
RUN chmod 0755 /entrypoint \  
&& useradd -U -M -s /usr/sbin/nologin -d /bitcoin bitcoin \  
&& mkdir -p /bitcoin/data \  
&& mkdir -p /bitcoin/.bitcoin \  
&& ln -s /etc/bitcoin.conf /bitcoin/.bitcoin/bitcoin.conf \  
&& chown -R bitcoin: /bitcoin  
VOLUME /bitcoin/data  
ENV HOME /bitcoin  
CMD ["/entrypoint"]  

