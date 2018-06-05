FROM debian:latest  
MAINTAINER Piotr Łuczak <piotrluczak1995@gmail.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r openttd --gid=999 && useradd -r -g openttd --uid=999 openttd  
  
# Download all dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
libfontconfig1 \  
libfreetype6 \  
liblzo2-2 \  
libpng12-0 \  
libsdl1.2debian \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates \  
&& apt-get clean  
  
ENV OPENTTD_VERSION 1.6.1  
ENV OPENGFX_VERSION 0.5.4  
# Download and install openttd  
RUN wget
http://binaries.openttd.org/releases/${OPENTTD_VERSION}/openttd-${OPENTTD_VERSION}-linux-
ubuntu-trusty-amd64.deb \  
&& dpkg -i openttd-${OPENTTD_VERSION}-linux-ubuntu-trusty-amd64.deb \  
&& rm openttd-${OPENTTD_VERSION}-linux-ubuntu-trusty-amd64.deb  
  
# Download OpenGFX  
RUN mkdir -p /usr/share/games/openttd/baseset/ \  
&& cd /usr/share/games/openttd/baseset/ \  
&& wget
http://bundles.openttdcoop.org/opengfx/releases/LATEST/opengfx-${OPENGFX_VERSION}.zip
\  
&& unzip opengfx-${OPENGFX_VERSION}.zip \  
&& tar -xvf opengfx-${OPENGFX_VERSION}.tar \  
&& rm opengfx-${OPENGFX_VERSION}.zip opengfx-${OPENGFX_VERSION}.tar \  
&& cd -  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME /home/openttd/.openttd  
EXPOSE 3979/tcp  
EXPOSE 3979/udp  
CMD ["/usr/games/openttd"]  

