# Mysql:5.7 at 21.03.2018  
FROM
mysql@sha256:691c55aabb3c4e3b89b953dd2f022f7ea845e5443954767d321d5f5fa394e28c  
  
LABEL maintainer="b.eyselein@gmail.com"  
  
ARG FILE=init.sql  
  
ENV MYSQL_ROOT_PASSWORD="sT8aV#k7" MYSQL_USER="it4all"
MYSQL_PASSWORD="sT8aV#k7"  
COPY ./$FILE /docker-entrypoint-initdb.d/sql_init.sql

