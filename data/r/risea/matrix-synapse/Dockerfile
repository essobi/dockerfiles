FROM debian:stretch-slim  
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r synapse && useradd -r -g synapse synapse  
  
# Git branch to build from  
ARG SYNAPSE_VERSION=v0.27.4  
ARG SYNAPSE_REST_AUTH=v0.1.1  
# use --build-arg REBUILD=$(date) to invalidate the cache and upgrade all  
# packages  
ARG REBUILD=1  
RUN set -ex \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& mkdir -p /var/cache/apt/archives \  
&& touch /var/cache/apt/archives/lock \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
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
python-setuptools \  
python-virtualenv \  
sqlite \  
zlib1g \  
zlib1g-dev \  
&& pip install --upgrade pip==9.0.3 \  
python-ldap \  
pyopenssl \  
enum34 \  
ipaddress \  
lxml \  
supervisor \  
&& git clone --branch $SYNAPSE_VERSION --depth 1 https://github.com/matrix-
org/synapse.git \  
&& cd /synapse \  
&& pip install --upgrade . \  
&& mv res/templates /synapse_templates \  
&& cd / \  
&& rm -rf /synapse \  
&& git clone --branch $SYNAPSE_REST_AUTH --depth 1
https://github.com/maxidor/matrix-synapse-rest-auth.git \  
&& cd matrix-synapse-rest-auth \  
&& cp rest_auth_provider.py /usr/lib/python2.7/dist-packages/ \  
&& cd .. \  
&& rm -rf matrix-synapse-rest-auth \  
&& apt-get autoremove -y \  
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
&& rm -rf /var/lib/apt/* /var/cache/apt/*  
  
RUN mkdir /data \  
&& mkdir /uploads \  
&& chown synapse:synapse /data \  
&& chown synapse:synapse /uploads  
  
VOLUME /data  
VOLUME /uploads  
  
  
  
# add configs  
COPY config/supervisord-matrix.conf config/supervisord-turnserver.conf /conf/  
COPY config/index.html config/logo.png /webclient/  
COPY home_server_config.py docker-entrypoint.sh config/supervisord.conf /  
  
EXPOSE 8008 8448 3478  
WORKDIR /data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

