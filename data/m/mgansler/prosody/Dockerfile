FROM debian:jessie  
MAINTAINER martin@martingansler.de  
  
ENV DEBIAN_FRONTEND=noninteractive \  
PROSODY_VERSION="0.10_1nightly179-1"  
ADD
http://packages.prosody.im/debian/pool/main/p/prosody-0.10/prosody-$PROSODY_VERSION~jessie_amd64.deb
/tmp/  
  
RUN apt-get update && apt-get install --yes --no-install-recommends \  
lua5.1 \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-socket \  
lua-event \  
lua-sec \  
lua-zlib \  
libidn11 \  
liblua5.1-expat0 \  
liblua5.1-filesystem0 \  
openssl \  
&& dpkg -i /tmp/prosody-$PROSODY_VERSION~jessie_amd64.deb && service prosody
stop \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/etc/prosody"]  
  
EXPOSE 5222 5269 5280 5281  
CMD [ "prosodyctl", "start" ]  

