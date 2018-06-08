FROM prima/elixir-official:1.6.5  
  
RUN apt-get update && \  
apt-get install -qqy mysql-client && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

