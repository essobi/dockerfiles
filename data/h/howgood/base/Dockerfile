# HowGood Base Container  
# howgood/base  
  
FROM debian:jessie  
  
# Prevent documentation from being installed http://askubuntu.com/a/401144/518  
RUN cd /etc/dpkg/dpkg.cfg.d/ \  
&& echo 'path-exclude /usr/share/doc/*' >> 01_nodoc \  
&& echo 'path-include /usr/share/doc/*/copyright$' >> 01_nodoc \  
&& echo 'path-exclude /usr/share/man/*$' >> 01_nodoc \  
&& echo 'path-exclude /usr/share/groff/*$' >> 01_nodoc \  
&& echo 'path-exclude /usr/share/info/*$' >> 01_nodoc \  
&& echo 'path-exclude /usr/share/lintian/*$' >> 01_nodoc \  
&& echo 'path-exclude /usr/share/linda/*$' >> 01_nodoc  
# Install all of the base dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yf \  
autoconf \  
binutils \  
build-essential \  
ca-certificates \  
curl \  
gdal-bin \  
git \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libfreetype6-dev \  
libgeoip1 \  
libgeos-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblcms2-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmemcached-dev \  
libncurses-dev \  
libpq-dev \  
libproj-dev \  
libreadline-dev \  
libssl-dev \  
libsqlite3-dev \  
libtiff-dev \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
locales \  
postgis \  
socat \  
tcl8.5-dev \  
tk8.5-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y \  
&& apt-get autoremove -y  
  
# Configure the locale  
RUN dpkg-reconfigure locales \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& apt-get clean -y \  
&& apt-get autoremove -y  
  
ENV LC_ALL C.UTF-8  

