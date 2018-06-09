FROM mariadb  
MAINTAINER "Hiroki Takeyama"  
# timezone  
ENV TZ Asia/Tokyo  
  
# entrypoint  
RUN { \  
echo '#!/bin/bash -eu'; \  
echo '{'; \  
echo ' echo "[client]";'; \  
echo ' echo "default-character-set = ${MYSQL_CHARSET}";'; \  
echo ' echo "[mysqld]";'; \  
echo ' echo "init-connect = SET NAMES ${MYSQL_CHARSET}";'; \  
echo ' echo "collation-server = ${MYSQL_CHARSET}_unicode_ci";'; \  
echo ' echo "character-set-server = ${MYSQL_CHARSET}";'; \  
echo ' echo "skip-character-set-client-handshake";'; \  
echo '} > /etc/mysql/conf.d/charset.cnf'; \  
echo 'docker-entrypoint.sh "$@"'; \  
} > /usr/local/bin/my-entrypoint.sh  
RUN chmod +x /usr/local/bin/my-entrypoint.sh  
ENTRYPOINT ["my-entrypoint.sh"]  
  
# mysql character-set  
ENV MYSQL_CHARSET utf8mb4  
  
# mysql password  
ENV MYSQL_ROOT_PASSWORD root  
  
VOLUME /var/lib/mysql  
  
EXPOSE 3306  
CMD ["mysqld"]  

