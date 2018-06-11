FROM mariadb:10.3  
RUN apt-get update && apt-get install -y galera-arbitrator-3 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY galera-entrypoint.sh /  
  
ENTRYPOINT ["/galera-entrypoint.sh"]  
CMD ["mysqld"]

