FROM prima/proxysql:1.3.0f  
  
RUN apt-get update && \  
apt-get install -y awscli mysql-client curl && \  
rm -r /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["proxysql", "-f", "--initial", "-c", "/etc/proxysql.cfg"]  

