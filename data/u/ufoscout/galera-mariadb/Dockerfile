FROM mariadb:10.3  
RUN apt-get update && apt-get install -y galera-3 galera-arbitrator-3 rsync  
RUN apt-get autoclean  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD https://github.com/ufoscout/docker-compose-
wait/releases/download/2.2.1/wait /wait  
RUN chmod +x /wait  
  
COPY galera-entrypoint.sh /  
RUN chmod +x /galera-entrypoint.sh  
  
EXPOSE 3306 4444 4567 4567/udp 4568  
ENTRYPOINT ["/galera-entrypoint.sh"]  
CMD ["mysqld"]  

