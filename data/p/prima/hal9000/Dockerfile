FROM prima/elixir-official:1.6.5  
  
RUN curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add
- && \  
apt-get update && \  
apt-get install -qqy mysql-client postgresql-client-9.6 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

