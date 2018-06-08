# Dependencia para compilar con curl.  
FROM buildpack-deps:jessie-curl  
  
MAINTAINER Yohany Flores <yohanyflores@gmail.com>  
  
LABEL com.imolko.group=imolko  
LABEL com.imolko.type=base  
  
# Creamos el usuario gearman  
RUN useradd -b /var/lib/ -c "Gearman Job Server" -m -s /bin/false gearman  
  
# grab gosu for easy step-down from root  
# RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
# RUN wget --output-document /usr/local/bin/gosu.asc --quiet
"https://github.com/tianon/gosu/releases/download/1.5/gosu-$(dpkg --print-
architecture).asc" \  
# && wget --output-document /usr/local/bin/gosu --quiet
"https://github.com/tianon/gosu/releases/download/1.5/gosu-$(dpkg --print-
architecture)" \  
# && gpg --verify /usr/local/bin/gosu.asc \  
# && rm /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu  
  
ENV GEARMAN_VERSION "1.1.16"  
ENV GEARMAN_URL
"https://github.com/gearman/gearmand/releases/download/${GEARMAN_VERSION}/gearmand-${GEARMAN_VERSION}.tar.gz"  
ENV BUILD_PACKAGES gcc make g++ libboost-program-options-dev gperf libevent-
dev uuid-dev libmysqlclient-dev file libssl-dev  
#libboost-all-dev  
#Configuramos la zona horaria  
RUN echo "America/Caracas" > /etc/timezone && dpkg-reconfigure -f
noninteractive tzdata  
  
RUN set -ex \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y --no-install-recommends ${BUILD_PACKAGES} \  
&& curl -L ${GEARMAN_URL} -o gearmand.tar.gz \  
&& mkdir -p /usr/src/gearmand \  
&& tar -zxf gearmand.tar.gz -C /usr/src/gearmand --strip-components=1 \  
&& rm gearmand.tar.gz \  
&& cd /usr/src/gearmand \  
&& ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-mysql=yes \  
\--with-postgresql=no \  
\--with-sqlite3=no \  
\--disable-libmemcached \  
\--disable-libdrizzle \  
\--disable-libtokyocabinet \  
\--disable-libpq \  
\--enable-ssl \  
\--enable-jobserver=no \  
\--disable-hiredis \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/gearmand \  
&& apt-get remove --purge -y --force-yes $BUILD_PACKAGES \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER gearman  
EXPOSE 4730  
CMD ["--verbose", "NOTICE", "--job-retries", "10", "--log-file", "stderr", "--
threads", "16", "--keepalive", "--keepalive-idle", "500", "--keepalive-
interval", "60", "--keepalive-count", "60" ]  

