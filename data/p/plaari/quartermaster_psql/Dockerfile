# 2015-10-25  
# PostgreSQL server for Quartermaster project  
FROM ubuntu  
MAINTAINER aaryndo@gmail.com  
  
RUN apt-get update && apt-get install -y postgresql-9.3  
  
USER postgres  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "local all postgres peer" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
# TODO [MC][2015-10-25] Create PSQL logs purging mechanism  
  
CMD /usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c
config_file=/etc/postgresql/9.3/main/postgresql.conf  
  

