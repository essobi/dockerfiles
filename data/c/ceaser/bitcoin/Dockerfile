FROM debian:jessie-slim  
MAINTAINER Ceaser Larry  
  
# Set build arguments.  
ARG DEB_PROXY  
ENV DEB_PROXY ${DEB_PROXY}  
  
# Optional APT Proxy  
RUN [ -z "$DEB_PROXY" ] || \  
echo "Acquire::http::Proxy \"$DEB_PROXY\";" > /etc/apt/apt.conf.d/01proxy && \  
echo "Acquire::https::Proxy false;" >> /etc/apt/apt.conf.d/01proxy  
  
ENV GOSU_VERSION 1.10  
  
RUN set -ex \  
# Install dependencies.  
&& apt-get update \  
&& apt-get install -y \  
gnupg \  
netcat \  
ca-certificates \  
wget \  
  
# install gosu  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
  
# verify the signature  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch \--verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
  
# test gosu works  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
  
# setup bitcoin  
&& installDir="$(mktemp -d)" \  
&& cd "$installDir" \  
&& wget -qO "bitcoin-0.15.1-x86_64-linux-gnu.tar.gz"
"https://bitcoincore.org/bin/bitcoin-core-0.15.1/bitcoin-0.15.1-x86_64-linux-
gnu.tar.gz" \  
&& echo "387c2e12c67250892b0814f26a5a38f837ca8ab68c86af517f975a2a2710225b
bitcoin-0.15.1-x86_64-linux-gnu.tar.gz" > "SHA256SUMS" \  
&& sha256sum -c SHA256SUMS \  
&& tar xf bitcoin-0.15.1-x86_64-linux-gnu.tar.gz \  
&& cd $(find . -type d -name "bitcoin*" 2>/dev/null) \  
&& cp -R bin/* /usr/local/bin/ \  
&& cp -R include/* /usr/local/include/ \  
&& cp -R lib/* /usr/local/lib/ \  
&& cp -R share/* /usr/local/share/ \  
&& cd .. \  
&& cd .. \  
&& rm -rf "$installDir" \  
  
# cleanup  
&& apt-get purge -y apt-transport-https wget ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apt/apt.conf.d/01proxy  
# Copy entrypoint script.  
COPY /docker-entrypoint.sh /  
  
# Setup  
RUN set -xe \  
&& mkdir -p /data/.bitcoin \  
&& useradd -s /usr/sbin/nologin -r -M -d /data bitcoin \  
&& chown bitcoin:bitcoin -R /data  
# Set up healthcheck.  
HEALTHCHECK \--interval=5m \--timeout=30s \--retries=3 CMD nc -z 127.0.0.1
8333  
  
# Expose default server port.  
EXPOSE 8333/tcp  
  
# Set up a volume for configuration files and game save.  
VOLUME ["/data"]  
  
# Set entrypoint and default command.  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["usr/local/bin/bitcoind", "-printtoconsole"]  
  

