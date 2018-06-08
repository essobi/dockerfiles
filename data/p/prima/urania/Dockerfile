FROM prima/elixir-official:1.6.5-19  
  
RUN apt-get update && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

