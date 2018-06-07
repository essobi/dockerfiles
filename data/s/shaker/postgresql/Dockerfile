FROM ubuntu:14.04  
MAINTAINER Shaker Qawasmi - github.com/sqawasmi  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Configure locale  
RUN locale-gen en_US.UTF-8 && update-locale  
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y openssh-server supervisor  
RUN apt-get -y install python-software-properties software-properties-common
postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
RUN echo 'root:postgres' |chpasswd  
ADD files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
USER postgres  
  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\  
createdb -O docker docker  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
USER root  
  
EXPOSE 22 5432  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["/usr/bin/supervisord"]  

