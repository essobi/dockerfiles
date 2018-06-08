FROM prima/elixir-official:1.5.3-2  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.6" >
"/etc/apt/sources.list.d/postgresql.list" && \  
curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&
\  
apt-get update && \  
apt-get install -qqy postgresql-client-9.6 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

