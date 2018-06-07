FROM postgres:9.5  
MAINTAINER LinShare <linshare@linagora.com>  
  
EXPOSE 5432  
ARG VERSION="2.1.1"  
ARG CHANNEL="releases"  
arg EXT="com"  
RUN apt-get update && apt-get install wget unzip -y && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN
URL="https://nexus.linagora.${EXT}/service/local/artifact/maven/content?r=linshare-${CHANNEL}&g=org.linagora.linshare&a=linshare-
core&c=sql&v=${VERSION}"; \  
wget --no-check-certificate --progress=bar:force:noscroll \  
-O linshare.tar.bz2 "${URL}&p=tar.bz2" \  
&& wget --no-check-certificate --progress=bar:force:noscroll \  
-O linshare.tar.bz2.sha1 "${URL}&p=tar.bz2.sha1" \  
&& sed -i 's#^\\(.*\\)#\1\tlinshare.tar.bz2#' linshare.tar.bz2.sha1 \  
&& sha1sum -c linshare.tar.bz2.sha1 --quiet && rm -f linshare.tar.bz2.sha1  
  
RUN tar -xvjf linshare.tar.bz2 \  
linshare-core-sql/postgresql/createSchema.sql \  
linshare-core-sql/postgresql/import-postgresql.sql \  
&& ln -s linshare-core-sql/postgresql/* . \  
&& rm -f linshare.tar.bz2  
  
COPY createDatabase.sql /docker-entrypoint-initdb.d/00_createDatabase.sql  
  
COPY init-pg.sh /docker-entrypoint-initdb.d/01_init-pg.sh  
  

