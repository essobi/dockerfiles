FROM python:3.5  
MAINTAINER Olivier Tabone <olivier.tabone@ripplemotion.fr>  
  
ENV C_INCLUDE_PATH /usr/include/gdal/  
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y apt-transport-https \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
libgdal-dev \  
swig \  
postgresql-client \  
protobuf-compiler \  
libprotoc-dev \  
locales \  
osmosis \  
libgeoip-dev geoip-database-extra \  
yarn \  
nodejs \  
netcat \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& (cd /usr/bin && ( [ -e node ] || ln -s nodejs node ))  
  
RUN set -x \  
&& mkdir -p ~/.ssh \  
&& ssh-keyscan -t rsa bitbucket.org > ~/.ssh/known_hosts \  
&& chmod 644 ~/.ssh/known_hosts  
  
RUN set -x \  
&& pip install --upgrade pip virtualenv setuptools wheel tox  

