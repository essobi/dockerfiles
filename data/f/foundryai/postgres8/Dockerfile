FROM debian:jessie  
  
RUN groupadd -r postgres --gid=999 \  
&& useradd -r -g postgres --uid=999 postgres  
  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
build-essential \  
libreadline6 \  
libreadline6-dev \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN mkdir /downloads \  
&& cd /downloads \  
&& wget https://ftp.postgresql.org/pub/source/v8.0.2/postgresql-8.0.2.tar.gz \  
&& tar -xzf postgresql-8.0.2.tar.gz \  
&& cd postgresql-8.0.2 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /downloads  
  
ENV PATH /usr/local/pgsql/bin:$PATH  
  
ENV PGDATA /var/lib/pgsql/data  
VOLUME /var/lib/pgsql/data  
  
COPY postgresql.conf pg_hba.conf /config/  
COPY docker-entrypoint.sh /  
  
ENV POSTGRES_USER postgres  
ENV POSTGRES_DATABASE postgres  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postmaster"]  

