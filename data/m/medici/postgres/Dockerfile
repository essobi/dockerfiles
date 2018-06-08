FROM mdillon/postgis:9.6-alpine  
  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
postgresql-contrib  
  
COPY ./init-db.sh /docker-entrypoint-initdb.d/postgis.sh

