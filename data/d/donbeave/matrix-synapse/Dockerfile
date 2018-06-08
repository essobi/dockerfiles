FROM debian:stretch-slim  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r synapse && useradd -r -g synapse synapse  
  
# add supervisor configs  
COPY config/supervisord-matrix.conf /conf/  
COPY config/supervisord-turnserver.conf /conf/  
COPY config/supervisord.conf /  
  
# Git branch to build from  
ARG SYNAPSE_VERSION=v0.25.0  
  
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
git clone --branch $SYNAPSE_VERSION --depth 1 https://github.com/matrix-
org/synapse.git \  
&& cd /synapse \  
&& pip install --upgrade . \  
&& cd / \  
&& rm -rf /synapse \  
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
  
COPY config/index.html /webclient/  
COPY config/logo.png /webclient/  
COPY home_server_config.py /home_server_config.py  
  
RUN mkdir /data \  
&& mkdir /uploads \  
&& chown synapse:synapse /data \  
&& chown synapse:synapse /uploads  
  
VOLUME /data  
VOLUME /uploads  
  
WORKDIR /data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8008 8448 3478  
CMD ["start"]  

