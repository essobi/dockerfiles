FROM mariadb  
MAINTAINER Joshua <joshua7v@hotmail.com>  
  
RUN { \  
echo '[mysqld]'; \  
echo 'character-set-server=utf8'; \  
echo 'collation-server=utf8_general_ci'; \  
echo '[client]'; \  
echo 'default-character-set=utf8'; \  
} > /etc/mysql/conf.d/charset.cnf  
  

