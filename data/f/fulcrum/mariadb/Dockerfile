FROM fulcrum/alpine  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
echo '@community http://dl-cdn.alpinelinux.org/alpine/edge/community/' >>
/etc/apk/repositories && \  
apk update && apk upgrade && \  
apk add bash gosu@testing mariadb mariadb-client shadow@community tzdata && \  
mkdir /docker-entrypoint-initdb.d /run/mysqld && \  
chown mysql.mysql /run/mysqld  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

