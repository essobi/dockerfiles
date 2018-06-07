FROM debian:jessie  
MAINTAINER Christopher Hiller <boneskull@boneskull.com>  
  
ENV HAPI_VERSION 8.8.1  
ENV DIGS_VERSION devel  
ENV DISTRO jessie  
ENV APT_DEPS curl apt-transport-https ca-certificates  
ENV RUNTIME_DEPS iojs  
ENV BUILD_DEPS gcc make git g++ python  
  
RUN useradd -d /usr/local/digs -m -s /bin/bash digs  
RUN chown -R digs:digs /usr/local/digs  
WORKDIR /usr/local/digs  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y $APT_DEPS \--no-install-recommends \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/iojs_2.x $DISTRO main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/iojs_2.x $DISTRO main" >>
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update \  
&& gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get install -y $RUNTIME_DEPS $BUILD_DEPS \--no-install-recommends \  
&& gosu digs npm install hapi@$HAPI_VERSION \  
&& gosu digs npm install digs@$DIGS_VERSION \  
&& npm install -g pm2 \  
&& apt-get purge -y $BUILD_DEPS $APT_DEPS \  
&& apt-get autoremove -y \  
&& rm -f /usr/local/bin/gosu  
USER digs  
WORKDIR /usr/local/digs  
RUN mkdir -p /usr/local/digs/log  
ENTRYPOINT ["pm2"]  
CMD ["start", "node_modules/.bin/digs", "--name", "digs", "--log",
"log/pm2.log", "--watch", "--no-daemon"]  

