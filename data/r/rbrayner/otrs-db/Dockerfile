FROM mariadb:10.3  
#RUN sed -i 's/^\\(max_allowed_packet\s*=\s*\\).*$/\120M/' /etc/mysql/my.cnf  
#RUN sed -i 's/^\\(query_cache_size\s*=\s*\\).*$/\132M/' /etc/mysql/my.cnf  
#RUN sed -i 's/^\\(innodb_log_file_size\s*=\s*\\).*$/\1256M/'
/etc/mysql/my.cnf  
  
RUN echo "[mysqld]" > /etc/mysql/conf.d/otrs.cnf  
RUN echo "max_allowed_packet = 120M" >> /etc/mysql/conf.d/otrs.cnf  
RUN echo "query_cache_size = 132M" >> /etc/mysql/conf.d/otrs.cnf  
RUN echo "innodb_log_file_size = 1256M" >> /etc/mysql/conf.d/otrs.cnf  
  
RUN echo "character-set-server=utf8" >> /etc/mysql/conf.d/otrs.cnf  
  
RUN echo "collation-server=utf8_general_ci" >> /etc/mysql/conf.d/otrs.cnf  
  
EXPOSE 3306  

