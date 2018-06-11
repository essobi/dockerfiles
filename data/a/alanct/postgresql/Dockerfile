# DOCKER-VERSION 0.6.4  
FROM ubuntu:12.04  
RUN apt-get update  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository -y ppa:pitti/postgresql  
RUN apt-get update  
RUN apt-get -y install postgresql-9.2 postgresql-client-9.2 postgresql-
contrib-9.2  
  
RUN su postgres -c '/usr/lib/postgresql/9.2/bin/postgres --single -c config-
file=/etc/postgresql/9.2/main/postgresql.conf <<< "alter user postgres with
password '"'"'docker'"'"';"'  
RUN echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.2/main/pg_hba.conf  
  
EXPOSE 5432  
CMD ["su", "postgres", "-c", "/usr/lib/postgresql/9.2/bin/postgres -c config-
file=/etc/postgresql/9.2/main/postgresql.conf -c listen-addresses=*"]  

