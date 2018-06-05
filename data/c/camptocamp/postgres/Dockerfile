FROM postgres:10  
RUN apt-get update \  
&& for POSTGIS_VERSION in 2.4; do \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
postgresql-contrib \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION-scripts \  
postgresql-$PG_MAJOR-pgrouting; \  
done \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# allow the container to be started with `--user`  
RUN chmod g=u /etc/passwd \  
&& sed -i '/# allow the container to be started with `--user`/a if ! whoami &>
/dev/null; then\n\tif [ -w /etc/passwd ]; then\n\t\techo
"${USER_NAME:-default}:x:$(id -u):0:${USER_NAME:-default}
user:${HOME}:/sbin/nologin" >> /etc/passwd\n\tfi\nfi' /usr/local/bin/docker-
entrypoint.sh  

