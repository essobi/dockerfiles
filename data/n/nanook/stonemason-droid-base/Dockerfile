FROM debian:jessie  
MAINTAINER WeiLiang Qian <gliese.q@gmail.com>  
LABEL Description="Base image for geo data authorization."  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV STONEMASON_DROID_HOME=/var/lib/droid/  
WORKDIR $STONEMASON_DROID_HOME  
  
RUN set -x \  
\  
  
# install components  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
locales \  
curl \  
make \  
gdal-bin \  
python-gdal \  
python-pip \  
postgresql-client \  
postgresql-client-common \  
postgis \  
&& pip install awscli \  
\  
  
# setup locale  
&& dpkg-reconfigure locales \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \  
&& locale-gen \  
  
# setup imposm3  
&& mkdir -p bin \  
&& curl -sSL
http://cdn.knrdesign.co/dist/imposm/imposm3-0.1dev-20160128-bb3d003-linux-x86-64.tar.gz
| tar xfz - \  
&& ln -sf `pwd`/imposm3-0.1dev-20160128-bb3d003-linux-x86-64/* bin/  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
PATH=$STONEMASON_DROID_HOME/bin:$PATH  
  
COPY docker-init.sh ./  
  
# test installation  
RUN set -x \  
&& python -c 'import gdal; print("GDAL Version:", gdal.VersionInfo())' \  
&& imposm3 version \  
&& psql --version  

