FROM debian:testing  
  
# inspired from the official prosody image https://github.com/prosody/prosody-
docker/blob/master/Dockerfile  
MAINTAINER Andreas Linz <klingt.net@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y curl  
RUN echo "deb http://packages.prosody.im/debian stable main" >>
/etc/apt/sources.list  
RUN curl -Ls "https://prosody.im/files/prosody-debian-packages.key" | apt-key
add -  
RUN apt-key update &&\  
apt-get install -y\  
curl \  
openssl \  
lua5.1 \  
libidn11 \  
libssl1.0.0 \  
lua-dbi-sqlite3 \  
lua-event \  
lua-expat \  
lua-filesystem \  
lua-sec \  
lua-socket \  
lua-zlib \  
prosody &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -i 's/^daemonize = true/daemonize = false/g'
/etc/prosody/prosody.cfg.lua &&\  
sed -i 's/^log = {/log = { { to = "console" };/g' /etc/prosody/prosody.cfg.lua
&&\  
mkdir -p /var/run/prosody &&\  
chown -R prosody:prosody /etc/prosody /var/log/prosody /var/lib/prosody
/var/run/prosody  
  
EXPOSE 80\  
443  
# XMPP client2server, server2server  
EXPOSE 5222\  
5269  
# XMPP BOSH websocket (HTTP/HTTPS)  
EXPOSE 5280\  
5281  
# XMPP external components  
EXPOSE 5347  
  
VOLUME /etc/prosody \  
/var/log/prosody \  
/var/lib/prosody  

