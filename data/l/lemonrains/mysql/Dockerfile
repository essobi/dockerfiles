FROM mysql  
  
MAINTAINER lemon <lemonrains@163.com>  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

