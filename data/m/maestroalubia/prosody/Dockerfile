################################################################################  
# Build a dockerfile for Prosody XMPP server  
# Based on debian  
################################################################################  
  
FROM debian:jessie  
  
RUN groupadd -r prosody && useradd -r -g prosody prosody  
  
# Install dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
gnupg \  
libidn11 \  
libidn11-dev \  
libssl1.0.0 \  
libssl-dev \  
lua-bitop \  
lua-bitop-dev \  
lua-dbi-mysql \  
lua-dbi-mysql-dev \  
lua-dbi-postgresql \  
lua-dbi-postgresql-dev \  
lua-dbi-sqlite3 \  
lua-dbi-sqlite3-dev \  
lua-event \  
lua-event-dev \  
lua-expat \  
lua-expat-dev \  
lua-filesystem \  
lua-filesystem-dev \  
lua-sec \  
lua-sec-dev \  
lua-socket \  
lua-socket-dev \  
lua-zlib \  
lua-zlib-dev \  
lua5.1 \  
lua5.1-0-dev \  
mercurial \  
openssl \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY pgp_keys.asc .  
  
RUN gpg --import pgp_keys.asc  
  
RUN mkdir -p /var/log/prosody /var/run/prosody \  
&& touch /var/log/prosody/prosody.log \  
&& touch /var/log/prosody/prosody.err \  
&& chown -R prosody:prosody /var/log/prosody /var/run/prosody  
  
# Install and configure prosody  
ARG PROSODY_VERSION=0.10.0  
RUN curl -o prosody.tar.gz
https://prosody.im/downloads/source/prosody-${PROSODY_VERSION}.tar.gz \  
&& curl -o signature.asc
https://prosody.im/downloads/source/prosody-${PROSODY_VERSION}.tar.gz.asc \  
&& gpg --verify signature.asc prosody.tar.gz \  
&& mkdir -p /usr/src/prosody \  
&& tar -x --strip-components=1 -C /usr/src/prosody -f prosody.tar.gz \  
&& cd /usr/src/prosody \  
&& ./configure --ostype=debian --prefix="/usr" --sysconfdir="/etc/prosody"
--datadir="/var/lib/prosody" \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/prosody  
  
VOLUME /var/lib/prosody  
  
COPY ./entrypoint.sh /entrypoint.sh  
COPY create_dhparam.sh /create_dhparam.sh  
COPY init_modules.sh /init_modules.sh  
COPY update_modules.sh /update_modules.sh  
RUN chmod 755 /entrypoint.sh  
  
USER prosody  
ENV __FLUSH_LOG yes  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 80 443 5222 5269 5347 5280 5281  
CMD ["prosody"]  

