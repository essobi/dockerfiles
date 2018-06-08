FROM debian:stretch-slim  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r sydent && useradd -r -d /data -M -g sydent sydent  
  
# Git branch to build from  
ARG SYDENT_VERSION=master  
  
# use --build-arg REBUILD=$(date) to invalidate the cache and upgrade all  
# packages  
ARG REBUILD=1  
RUN set -ex \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& mkdir -p /var/cache/apt/archives \  
&& touch /var/cache/apt/archives/lock \  
&& apt-get clean \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
bash \  
coreutils \  
coturn \  
file \  
gcc \  
git \  
libevent-2.0-5 \  
libevent-dev \  
libffi-dev \  
libffi6 \  
libgnutls28-dev \  
libjpeg62-turbo \  
libjpeg62-turbo-dev \  
libldap-2.4-2 \  
libldap2-dev \  
libsasl2-dev \  
libsqlite3-dev \  
libssl-dev \  
libssl1.0.2 \  
libtool \  
libxml2 \  
libxml2-dev \  
libxslt1-dev \  
libxslt1.1 \  
linux-headers-amd64 \  
make \  
pwgen \  
python \  
python-dev \  
python-pip \  
python-psycopg2 \  
python-virtualenv \  
sqlite \  
zlib1g \  
zlib1g-dev \  
; \  
pip install --upgrade pip ;\  
pip install --upgrade python-ldap ;\  
pip install --upgrade pyopenssl ;\  
pip install --upgrade enum34 ;\  
pip install --upgrade ipaddress ;\  
pip install --upgrade lxml ;\  
pip install --upgrade supervisor \  
; \  
git clone --branch $SYDENT_VERSION --depth 1 https://github.com/matrix-
org/sydent.git \  
&& cd /sydent \  
&& pip install --upgrade . \  
&& mkdir -p /init/sql \  
&& cp /sydent/sydent/db/*.sql /init/sql \  
&& cd / \  
&& rm -rf /sydent \  
; \  
apt-get autoremove -y \  
file \  
gcc \  
git \  
libevent-dev \  
libffi-dev \  
libjpeg62-turbo-dev \  
libldap2-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt1-dev \  
linux-headers-amd64 \  
make \  
python-dev \  
zlib1g-dev \  
; \  
apt-get autoremove -y ;\  
rm -rf /var/lib/apt/* /var/cache/apt/*  
  
RUN mkdir /data && chown -R sydent:sydent /data  
VOLUME /data  
WORKDIR /data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8090  
CMD ["start"]  

