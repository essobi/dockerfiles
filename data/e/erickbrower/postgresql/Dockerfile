FROM erickbrower/base:ubuntu_13.10  
  
RUN apt-get -qq update && apt-get install -y postgresql postgresql-9.1-postgis  
  
ADD pg_hba.conf /etc/postgresql/9.1/main/pg_hba.conf  
ADD postgresql.conf /etc/postgresql/9.1/main/postgresql.conf  
  
RUN chmod og-rwx /var/lib/postgresql/9.1/main/server.key && chown postgres
/var/lib/postgresql/9.1/main/server.key  
  
USER postgres  
  
EXPOSE 5432  
  
CMD ["/usr/lib/postgresql/9.1/bin/postgres", "-D",
"/var/lib/postgresql/9.1/main", "-c",
"config_file=/etc/postgresql/9.1/main/postgresql.conf", "-c",
"listen_addresses=*"]  

