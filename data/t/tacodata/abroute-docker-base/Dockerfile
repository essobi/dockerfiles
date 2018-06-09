#  
# this is the base image for all images  
# in this group. the main things are shared  
#  
FROM phusion/baseimage  
  
MAINTAINER Greg Fausak <greg@tacodata.com>  
  
ENV PG_VERSION 9.4  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update \  
&& apt-get install -y postgresql-${PG_VERSION} \  
postgresql-client-${PG_VERSION} \  
postgresql-server-dev-${PG_VERSION} \  
postgresql-contrib-${PG_VERSION} pwgen \  
python-dev python-pip \  
&& pip install sqlauth \  
&& rm -rf /var/lib/postgresql \  
&& rm -rf /var/lib/apt/lists/* \  
&& (cd /etc/postgresql; tar czvf /usr/lib/postgresql/etc.tar.gz .)  
  
  
COPY abenv /usr/local/etc/  

