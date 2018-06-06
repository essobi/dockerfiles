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
apt-transport-https \  
gnupg \  
ca-certificates \  
netcat \  
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
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
  
# test gosu works  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
  
# setup zcash sources  
&& wget -qO - https://apt.z.cash/zcash.asc | apt-key add \- \  
&& echo "deb [arch=amd64] https://apt.z.cash/ jessie main" >>
/etc/apt/sources.list.d/zcash.list \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
zcash \  
  
# cleanup  
&& apt-get purge -y apt-transport-https \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apt/apt.conf.d/01proxy  
  
# Copy entrypoint script.  
COPY /docker-entrypoint.sh /  
  
# Setup  
RUN set -xe \  
&& mkdir -p /data/.zcash \  
&& useradd -s /usr/sbin/nologin -r -M -d /data zcash \  
&& chown zcash:zcash -R /data  
  
# Set up healthcheck.  
HEALTHCHECK \--interval=5m --timeout=30s --retries=3 CMD nc -z 127.0.0.1 8233  
  
# Expose default server port.  
EXPOSE 8233/tcp  
  
# Set up a volume for configuration files and game save.  
VOLUME ["/data"]  
  
# Set entrypoint and default command.  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["usr/bin/zcashd", "-printtoconsole"]  
  

