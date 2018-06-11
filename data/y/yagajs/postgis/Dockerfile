FROM postgres:10  
  
ARG POSTGIS_VERSION=2.4.0  
ARG POSTGRES_MAJOR_VERSION=10  
  
MAINTAINER Arne Schubert, atd.schubert@gmail.com  
  
RUN set -x \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
curl build-essential libxml2-dev libgdal-dev libproj-dev libjson-c-dev
xsltproc docbook-xsl docbook-mathml \  
postgresql-server-dev-$POSTGRES_MAJOR_VERSION \  
\  
&& curl -L http://geos.osgeo.org/snapshots/geos-`date -d yesterday
+%Y%m%d`.tar.bz2 | tar xj -C /tmp \  
&& cd /tmp/geos-`date -d yesterday +%Y%m%d` \  
&& ./configure && make && make install \  
\  
&& curl -L http://postgis.net/stuff/postgis-$POSTGIS_VERSION.tar.gz | tar xz
-C /tmp \  
&& cd /tmp/postgis-$POSTGIS_VERSION/ \  
&& ./configure && make && make install && ldconfig && make comments-install \  
\  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  

