FROM ubuntu:12.04  
MAINTAINER Nate West <natescott.west@gmail.com>  
  
RUN apt-get update  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get -y install curl  
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
RUN apt-get update  
RUN apt-get -y install postgresql-9.3  
  
RUN su postgres -c '/usr/lib/postgresql/9.3/bin/postgres --single -c config-
file=/etc/postgresql/9.3/main/postgresql.conf <<< "alter user postgres with
password '"'"'docker'"'"';"'  
RUN echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf  
  
EXPOSE 5432  
CMD ["su", "postgres", "-c", "/usr/lib/postgresql/9.3/bin/postgres -c config-
file=/etc/postgresql/9.3/main/postgresql.conf -c listen-addresses=*"]  

