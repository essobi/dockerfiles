FROM mysql:latest  
  
RUN sed -i "/default-character-set/d" /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& sed -i "/\\[mysqld]/a skip-character-set-client-handshake"
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& sed -i "/\\[mysqld]/a collation-server=utf8mb4_unicode_ci"
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& sed -i "/\\[mysqld]/a character-set-server=utf8mb4"
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& sed -i "/\\[mysqld]/a init_connect= 'SET NAMES utf8mb4' "
/etc/mysql/mysql.conf.d/mysqld.cnf \  
&& sed -i "/\\[mysqld]/a init_connect=‘SET collation_connection =
utf8mb4_unicode_ci' " /etc/mysql/mysql.conf.d/mysqld.cnf  

