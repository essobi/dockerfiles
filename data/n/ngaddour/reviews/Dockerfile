FROM ubuntu:trusty  
MAINTAINER dev@onyme.com  
  
## add postgres group/user  
RUN groupadd -r postgres && useradd -r -g postgres postgres  
  
# verify PostgreSQL packages: PGP key must be the same as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# add PostgreSQL's repository for recent stable release  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.4" >
/etc/apt/sources.list.d/pgdg.list  
  
# update index && install Postgres + python dep  
RUN apt-get update  
RUN apt-get -y -q install python-software-properties software-properties-
common  
RUN apt-get -y -q install postgresql-plpython-9.4 postgresql-9.4 postgresql-
client-9.4 postgresql-contrib-9.4  
  
ENV PATH /usr/lib/postgresql/9.4/bin:$PATH  
  
# set Locale  
RUN update-locale "en_US.UTF-8"  
  
# run postgres service, create onyme role and reviews database with postgres
user  
USER postgres  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER onyme WITH SUPERUSER PASSWORD 'admin';" &&\  
createdb -O onyme reviews;  
  
# trust local/host connections with onyme role  
#NB: pourtant, je n'arrive pas à annuler la config par défaut (local all all
md5)  
RUN echo "host reviews onyme 0.0.0.0/0 trust" >>
/etc/postgresql/9.4/main/pg_hba.conf  
RUN echo "local reviews onyme trust" >> /etc/postgresql/9.4/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
  
## add postgres volume  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
## mount sql script for reviews insertion  
ADD amazon_review1998.sql /amazon_review1998.sql  
ADD setup_connection_db.sh /docker-entrypoint-initdb.d/setup_connection_db.sh  
  
# change to root user  
USER root  
RUN ["chown", "-R", "postgres", "/etc/init.d/"]  
RUN ["chmod", "755", "/etc/init.d/postgresql"]  
RUN ["chmod", "755", "/docker-entrypoint-initdb.d/setup_connection_db.sh"]  
  
# work around for AUFS bug  
# as per https://github.com/docker/docker/issues/783#issuecomment-56013588  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
# change to postgres user  
USER postgres  
  
# entrypoint script to setup db connection at container startup  
ENTRYPOINT ["/docker-entrypoint-initdb.d/setup_connection_db.sh"]  
  
# inputs for the entrypoint script  
CMD ["postgres", "/amazon_review1998.sql"]  
  
# Expose port  
EXPOSE 5432  

