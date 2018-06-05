FROM mdillon/postgis  
MAINTAINER Roman Scherer <roman@burningswell.com>  
  
ENV LEIN_ROOT 1  
ENV PATH "$PATH:/usr/local/bin  
  
ADD . /opt/burningswell/db  
WORKDIR /opt/burningswell/db  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install -y \--no-install-recommends ca-certificates curl
openjdk-8-jre-headless sqitch && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -s
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein && \  
chmod 755 /usr/local/bin/lein && \  
lein version  
  
ADD ./docker/bs-db-migrate.sh /docker-entrypoint-initdb.d/001-bs-db-migrate.sh  
ADD ./docker/bs-db-fixtures.sh /docker-entrypoint-initdb.d/002-bs-db-
fixtures.sh  
  
RUN lein uberjar  

