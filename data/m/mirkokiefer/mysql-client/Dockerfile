  
FROM mirkokiefer/ubuntu-base  
  
RUN apt-get install -y mysql-client  
  
ADD start_mysql_client.sh /start_mysql_client.sh  
  
CMD ["bash", "/start_mysql_client.sh"]  

