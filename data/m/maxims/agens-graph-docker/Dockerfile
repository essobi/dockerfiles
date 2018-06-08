FROM ubuntu:16.04  
# Install dependencies to enable building agens from source  
RUN apt-get update && apt-get -y -q install git build-essential libreadline-
dev zlib1g-dev flex bison \  
libxml2-dev libxslt-dev libssl-dev openssl libgnutls-openssl27 \  
libcrypto++-dev libldap2-dev libpam0g-dev tcl-dev python-dev  
  
RUN git clone https://github.com/bitnine-oss/agens-graph.git  
  
# Contrib package pg_hint_path requires agens be build first  
# So we exec install before install-world  
RUN cd /agens-graph \  
&& ./configure --prefix=`pwd` --with-tcl --with-pam --with-ldap --with-openssl
--with-libxml --with-libxslt \  
&& export PATH=$(pwd)/bin:$PATH \  
&& make install \  
&& make install-world  
  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
ENV PATH /agens-graph/bin:$PATH  
ENV PGDATA /agens-graph/data  
  
RUN mkdir -p /agens-graph/data && chown -R postgres agens-graph/data  
RUN chmod 700 /agens-graph/data  
RUN chown -R postgres /agens-graph/data  
VOLUME /agens-graph/data  
  
ENV GOSU_VERSION 1.10  
ENV PORT 5432  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
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
&& apt-get purge -y --auto-remove ca-certificates wget  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]

