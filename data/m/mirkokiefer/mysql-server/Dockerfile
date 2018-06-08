  
FROM mirkokiefer/ubuntu-base  
  
ADD install_mysql.sh /install_mysql.sh  
  
RUN bash /install_mysql.sh  
  
EXPOSE 3306  
CMD ["/usr/sbin/mysqld"]  

