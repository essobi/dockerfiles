FROM ubuntu:trusty  
MAINTAINER BRIDGE, JEROME <jeromebridge@pennassurancesoftware.com>  
  
# Ensure we create the cluster with UTF-8 locale  
RUN locale-gen en_US.UTF-8 && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
# Docker Workarounds?  
ENV DEBIAN_FRONTEND noninteractive  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
#Install PostgreSQL-9.3  
RUN apt-get update && \  
apt-get install -y postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
pwgen inotify-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Adjust PostgreSQL configuration so that remote connections to the database
are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
ADD modify_postgres_pass.sh ./modify_postgres_pass.sh  
ADD init_postgres_database.sh ./init_postgres_database.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 5432  
CMD ["/run.sh"]  

