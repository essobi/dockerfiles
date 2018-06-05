FROM prima/elixir-official:1.6.5  
  
RUN apt-get update && \  
apt-get install -qqy postgresql-client-9.6 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

