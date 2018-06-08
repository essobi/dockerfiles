FROM ubuntu  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.6 postgresql-client-9.6 postgresql-contrib-9.6  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.6/main/pg_hba.conf
&&\  
echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf  
  
USER postgres  
  
RUN /etc/init.d/postgresql start  
  
EXPOSE 5432  
VOLUME [ "/var/lib/postgresql" ]  
  
CMD [ "/usr/lib/postgresql/9.6/bin/postgres", "-D",
"/var/lib/postgresql/9.6/main", "-c",
"config_file=/etc/postgresql/9.6/main/postgresql.conf" ]  

