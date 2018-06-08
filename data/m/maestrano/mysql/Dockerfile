FROM mysql:5.7  
VOLUME ["/var/lib/mysql", "/snapshots"]  
  
# Set default charset to UTF-8  
COPY mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
# Point-in-time backup script with backup rotation  
COPY backup.sh /usr/local/bin/  
  
# MySQL server configuration  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

