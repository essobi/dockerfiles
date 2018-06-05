FROM postgres:9.5  
MAINTAINER Camptocamp "docker@camptocamp.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y --no-install-recommends --no-install-suggests install -t jessie-
pgdg postgresql-9.5-postgis-2.2 postgresql-9.5-postgis-2.2-scripts \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /custom-initdb.d  
  
COPY scripts/* /docker-entrypoint-initdb.d/  

