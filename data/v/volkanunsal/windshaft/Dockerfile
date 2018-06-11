#  
# Windshaft container  
#  
FROM phusion/baseimage:0.9.18  
MAINTAINER Volkan Unsal <spocksplanet@gmail.com>  
  
# Configuring locales  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update &&\  
apt-get install -y -q \  
build-essential \  
autoconf \  
automake \  
checkinstall \  
git-core \  
git \  
curl \  
bison \  
ca-certificates \  
gdal-bin \  
gnupg \  
imagemagick \  
libc6-dev \  
libcairo2-dev \  
libcurl4-gnutls-dev \  
libffi-dev \  
libgdal1-dev \  
libgeos-c1 \  
libgeos-dev \  
libgif-dev \  
libgdbm-dev \  
libgmp-dev \  
libicu-dev \  
libjpeg8-dev \  
libjson0 \  
libjson0-dev \  
libmapnik-dev \  
libpango1.0-dev \  
libpq5 \  
libpq-dev \  
libproj-dev \  
libreadline6 \  
libreadline6-dev \  
libssl-dev \  
libsqlite3-dev \  
libtool \  
libyaml-dev \  
libxml2-dev \  
libxslt-dev \  
mapnik-utils \  
ncurses-dev \  
openssl \  
pkg-config \  
proj-bin \  
proj-data \  
python2.7-dev \  
python-argparse \  
python-chardet \  
python-gdal \  
python-mapnik \  
python-simplejson \  
python-setuptools \  
sqlite3 \  
zlib1g \  
zlib1g-dev \  
\--no-install-recommends  
  
RUN git config --global user.email spocksplanet@gmail.com \  
&& git config --global user.name "Volkan Unsal"  
# Install NodeJS  
RUN curl
https://nodejs.org/download/release/v0.10.41/node-v0.10.41-linux-x64.tar.gz|
tar -zxf - --strip-components=1 -C /usr  
  
# Install NPM  
RUN npm install -g npm@1.4.29  
  
# Install Windshaft  
RUN git clone git://github.com/CartoDB/Windshaft-cartodb.git  
WORKDIR /Windshaft-cartodb  
RUN git reset --hard 03991319683452956ad5ceb2a1c95a452dbf3428 &&\  
./configure && npm install && mkdir logs  
  
# Assume the following linked services  
# - postgres:5432  
# - redis:6379  
# - varnish:6082 // <\- port to telnet interface  
# - varnish:6081 // <\- port to HTTP interface  
# - statsd:8125  
ADD ./config/WS-dev.js \  
/Windshaft-cartodb/config/environments/development.js  
  
EXPOSE 8181  
# Scripts  
RUN mkdir -p /etc/service/node  
ADD service/node.sh /etc/service/node/run  
  
CMD ["/sbin/my_init"]  
  
ENV GDAL_DATA /usr/share/gdal/1.10  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

