FROM mdillon/postgis:9.5  
RUN apt-get update \  
&& apt-get install -y build-essential wget postgresql-server-dev-9.5
libxml2-dev libproj-dev libgdal-dev libjson-c-dev libpcre3-dev postgresql-
plperl-9.5  
  
RUN cd tmp \  
&& wget http://download.osgeo.org/geos/geos-3.5.0.tar.bz2 \  
&& tar xfj geos-3.5.0.tar.bz2 \  
&& cd geos-3.5.0 \  
&& ./configure \  
&& make \  
&& make install  
  
RUN cd tmp \  
&& wget http://download.osgeo.org/postgis/source/postgis-2.2.2.tar.gz \  
&& tar xfz postgis-2.2.2.tar.gz \  
&& cd postgis-2.2.2 \  
&& ./configure \  
&& make \  
&& make install  
  
RUN rm -rf /tmp/postgis-* /tmp/geos-*  
RUN apt-get purge -y --auto-remove build-essential wget postgresql-server-
dev-9.5 libxml2-dev libproj-dev libgdal-dev libjson-c-dev libpcre3-dev  

