# vim:set ft=dockerfile:  
# Base on VRT Postgres Image  
FROM vrtsystems/postgres:develop  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
ENV PG_POSTGIS 2.1  
ENV PG_TEMPORAL 1.0.1  
RUN echo "=== Update package repository cache ====" \  
&& apt-get update \  
&& echo "=== Install dependencies ===============" \  
&& apt-get -y install build-essential \  
postgresql-server-dev-$PG_MAJOR=$PG_VERSION \  
postgresql-$PG_MAJOR-postgis-$PG_POSTGIS \  
pgxnclient \  
&& echo "=== Install temporal_tables extension ==" \  
&& pgxnclient install --testing "temporal_tables=${PG_TEMPORAL}" \  
&& echo "=== Cleaning up ========================" \  
&& apt-get -y purge postgresql-server-dev-$PG_MAJOR \  
build-essential pgxnclient \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& /usr/local/sbin/docker-cleanup.sh  
  
COPY 10_create_extensions.sh /usr/local/etc/docker-postgres/poststart-init.d/  

