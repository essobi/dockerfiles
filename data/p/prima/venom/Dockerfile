FROM prima/elixir-official:1.5.2  
  
RUN apt-get update && \  
apt-get install -qqy mysql-client && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

