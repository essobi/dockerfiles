FROM pascalgrimaud/ubuntu  
MAINTAINER Pascal Grimaud <pascalgrimaud@gmail.com>  
  
# update  
RUN apt-get -y update  
  
# installation : postgresql-9.3  
ENV PG_VERSION 9.3  
RUN apt-get -y install postgresql-${PG_VERSION} \  
postgresql-client-${PG_VERSION} \  
postgresql-contrib-${PG_VERSION}  
  
# configuration : remote connections to the database are possible  
RUN echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/${PG_VERSION}/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >>
/etc/postgresql/${PG_VERSION}/main/postgresql.conf  
  
# clean  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# expose ports  
EXPOSE 5432  
# volumes  
VOLUME ["/var/log/postgresql", "/var/lib/postgresql"]  
  
# add help  
ADD help.txt /help.txt  
ADD help /help  
RUN chmod 755 /help  
  
# script to start the container  
ADD postgresql_run.sh /postgresql_run.sh  
RUN chmod 755 /*.sh  
CMD ["/postgresql_run.sh"]  

