FROM prima/elixir-official:1.6.5  
# Timezone data  
RUN apt-get update && \  
apt-get install -qqy mysql-client postgresql-client && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

