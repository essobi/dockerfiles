FROM codeworksio/ubuntu:18.04-20180210  
# SEE: https://github.com/docker-library/postgres/blob/master/10/Dockerfile  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV PG_MAJOR="10" \  
PG_VERSION="10.2-1" \  
PATH="$PATH:/usr/lib/postgresql/10/bin" \  
PGDATA="/var/lib/postgresql/data"  
RUN set -ex; \  
\  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
\  
usermod -l postgres -m -d /home/postgres ubuntu; \  
groupmod -n postgres ubuntu; \  
\  
apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
"B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8"; \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main $PG_MAJOR"
> /etc/apt/sources.list.d/postgres.list; \  
apt-get --yes update; \  
apt-get --yes install \  
postgresql-$PG_MAJOR=$PG_VERSION \  
postgresql-common \  
; \  
sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf; \  
mv -v "/usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample"
/usr/share/postgresql/; \  
ln -sv ../postgresql.conf.sample "/usr/share/postgresql/$PG_MAJOR/"; \  
sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample; \  
mkdir -p /var/run/postgresql && chown -R postgres:postgres /var/run/postgresql
&& chmod 2777 /var/run/postgresql; \  
mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA"; \  
\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
COPY assets/ /  
  
WORKDIR /var/lib/postgresql/data  
VOLUME [ "/var/lib/postgresql/data" ]  
EXPOSE 5432  
CMD [ "postgres" ]  
  
### METADATA
###################################################################  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

