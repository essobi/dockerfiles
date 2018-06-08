################################################################################  
# Build a dockerfile for Prosody XMPP server  
# Based on ubuntu  
################################################################################  
  
FROM ubuntu:16.04  
  
MAINTAINER Lloyd Watkin <lloyd@evilprofessor.co.uk>  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
# Install dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
libidn11 \  
libssl1.0.0 \  
lua-bitop \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-event \  
lua-filesystem \  
lua-sec \  
lua-socket \  
lua-zlib \  
lua5.1 \  
openssl \  
prosody \  
prosody-modules \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i '1s/^/daemonize = false;\n/' /etc/prosody/prosody.cfg.lua \  
&& perl -i -pe 'BEGIN{undef $/;} s/^log = \\{.*?^\\}$/log = {\n {levels = {min
= "info"}, to = "console"};\n}/smg' \  
/etc/prosody/prosody.cfg.lua \  
  
# Install and configure prosody  
&& chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
ENV __FLUSH_LOG yes  
CMD ["prosody"]  

