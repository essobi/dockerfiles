FROM mariadb  
MAINTAINER SFoxDev <admin@sfoxdev.com>  
  
COPY config/my.cnf /etc/mysql/my.cnf  
ADD config /  
  
RUN chmod 775 /*.sh  
  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/run.sh"]  

