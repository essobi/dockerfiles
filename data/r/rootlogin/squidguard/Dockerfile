FROM rootlogin/squid  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ARG SQUIDGUARD_VERSION=1.4  
ARG
SQUIDGUARD_SHA512=6d55bda4c6b597ff52fed95ec336ca2d0b028359332217a552e645a3ac76d6d812926cd837e77cb5e046109c3c6291d52b92f3f7ac987dbf1b6fd17d68f1413d  
  
ARG BERKELEYDB_VERSION=4.5.20  
ARG
BERKELEYDB_SHA512=c34907a53323158627971f464c32b9a5b00aff0fa779c67117826ebeea86a4731e272a5dc6dc5ae32f16284ff15c79d93050273795381acaaefd48e18dc2d612  
  
ENV BLOCKLIST=http://www.shallalist.de/Downloads/shallalist.tar.gz  
ARG BLOCKED_CATEGORIES=adv,aggressive,porn,spyware,violence,warez  
  
ENV REDIRECT_URL=https://duckduckgo.com  
LABEL maintainer="Simon Erhardt <hello@rootlogin.ch>" \  
org.label-schema.name="SquidGuard" \  
org.label-schema.description="Minimal SquidGuard docker image with integrated
filter lists based on Alpine Linux." \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/chrootLogin/docker-squidguard" \  
org.label-schema.schema-version="1.0"  
RUN set -ex \  
# Install packages  
&& apk add --update \  
alpine-sdk \  
coreutils \  
python3 \  
wget \  
# Download BerkeleyDB  
&& wget -q http://download.oracle.com/berkeley-
db/db-${BERKELEYDB_VERSION}.tar.gz -O /tmp/db.tgz \  
&& echo "Verifying both integrity and authenticity of BerkeleyDB
${BERKELEYDB_VERSION}..." \  
&& CHECKSUM=$(sha512sum /tmp/db.tgz | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${BERKELEYDB_SHA512}" ]; then echo "Warning!
Checksum does not match!" && exit 1; fi \  
&& echo "All seems good, now unpacking BerkeleyDB ${BERKELEYDB_VERSION}..." \  
&& mkdir -p /usr/local/src/berkeley-db \  
&& tar xzf /tmp/db.tgz --strip-components=1 -C /usr/local/src/berkeley-db \  
&& cd /usr/local/src/berkeley-db/build_unix \  
&& ../dist/configure \  
&& make \  
&& make install \  
&& rm -rf /usr/local/src/berkeley-db \  
# Download SquidGuard  
&& wget -q
http://www.squidguard.org/Downloads/squidGuard-${SQUIDGUARD_VERSION}.tar.gz -O
/tmp/squidguard.tgz \  
&& echo "Verifying both integrity and authenticity of SquidGuard
${SQUIDGUARD_VERSION}..." \  
&& CHECKSUM=$(sha512sum /tmp/squidguard.tgz | awk '{print $1}') \  
&& if [ "${CHECKSUM}" != "${SQUIDGUARD_SHA512}" ]; then echo "Warning!
Checksum does not match!" && exit 1; fi \  
&& echo "All seems good, now unpacking SquidGuard ${SQUIDGUARD_VERSION}..." \  
&& mkdir -p /usr/local/src/squidguard \  
&& tar xzf /tmp/squidguard.tgz --strip-components=1 -C
/usr/local/src/squidguard \  
&& cd /usr/local/src/squidguard \  
# Compile SquidGuard  
&& ./configure --with-db=/usr/local/BerkeleyDB.4.5 \  
&& make \  
&& make install \  
&& rm -rf /usr/local/src/squidguard \  
# Remove build-time stuff  
&& apk del \  
alpine-sdk \  
coreutils \  
# Delete apk cache  
&& rm -rf /var/cache/apk/* \  
# Deleting temporary stuff  
&& rm -rf /tmp/*  
  
COPY root /  
  
ENV LD_LIBRARY_PATH=/usr/local/BerkeleyDB.4.5/lib  
  
RUN /create-blocklist.sh  

