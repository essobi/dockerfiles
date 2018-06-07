FROM ubuntu  
MAINTAINER matt  
  
# install prereqs  
RUN apt-get update  
RUN apt-get install -y python-software-properties software-properties-common
wget vim  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update  
  
# install postgres 9.2  
RUN apt-get install -y postgresql-9.3 postgresql-client-9.3 postgresql-
contrib-9.3  
  
# configure docker user/database  
ADD configure /configure  
RUN cat /configure  
RUN /bin/bash /configure  
  
# configure db  
ADD pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
ADD postgresql.conf /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
CMD ["/bin/su", "postgres", "-c", "/usr/lib/postgresql/9.3/bin/postgres -D
/var/lib/postgresql/9.3/main -c
config_file=/etc/postgresql/9.3/main/postgresql.conf"]  
  

