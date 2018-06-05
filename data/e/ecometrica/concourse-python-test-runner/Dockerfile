  
FROM ubuntu:xenial  
  
# Generate a locale so we get rid of ascii for postgres and some tests.  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
RUN update-locale LANG=en_US.utf8  
  
# Install gosu so we can run stuff as other users.  
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
&& apt-get install -y \  
build-essential \  
curl \  
gdal-bin \  
gettext \  
git \  
libcairo2-dev \  
libcairomm-1.0-1v5 \  
libcurl4-openssl-dev \  
libffi-dev \  
libfreetype6-dev \  
libjpeg62-dev \  
liblcms2-dev \  
libmemcached-dev \  
libpq-dev \  
libssl1.0.0 \  
memcached \  
mercurial \  
nodejs-legacy \  
npm \  
pgbouncer \  
postgresql \  
postgresql-9.5-postgis-2.2 \  
postgresql-client-9.5 \  
python \  
python-dev \  
python-httplib2 \  
python-pip \  
python-psycopg2 \  
python-vipscc \  
python-virtualenv \  
redis-server \  
screen \  
sudo \  
supervisor \  
vim \  
virtualenvwrapper \  
xmlsec1 \  
xvfb \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz > /tmp/wkhtmltox.tar.xz && \  
tar -C /usr --strip-components=1 -xvf /tmp/wkhtmltox.tar.xz && \  
rm /tmp/wkhtmltox.tar.xz

