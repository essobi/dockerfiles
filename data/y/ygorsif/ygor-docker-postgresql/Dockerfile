FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
postgresql-9.3 postgresql-contrib-9.3 libpq-dev python-software-properties
software-properties-common postgresql-client-9.3  
  
ADD postgresql.conf /etc/postgresql/9.3/main/postgresql.conf  
ADD pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
RUN chown postgres:postgres /etc/postgresql/9.3/main/*.conf  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
VOLUME ["/var/lib/postgresql"]  
EXPOSE 5432  
CMD ["/usr/local/bin/run"]  

