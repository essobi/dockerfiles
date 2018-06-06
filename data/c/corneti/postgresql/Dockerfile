FROM corneti/centos-dev:latest  
MAINTAINER Fabio Corneti <info@corneti.com>  
  
ENV PG_HOME /usr/pgsql-9.4  
ENV PGDATA /var/lib/pgsql/data  
ENV PATH $PG_HOME/bin:$PATH  
  
VOLUME ["/var/lib/pgsql"]  
  
RUN yum update -y && \  
yum install -y http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
redhat94-9.4-1.noarch.rpm && \  
yum groupinstall -y "PostgreSQL Database Server 9.4 PGDG" && \  
yum clean all  
  
ADD postgresql.conf /etc/pgsql/postgresql.conf  
ADD pg_hba.conf /etc/pgsql/pg_hba.conf  
RUN chown -R postgres /etc/pgsql  
ADD run.sh /usr/local/sbin/run.sh  
RUN chmod +x /usr/local/sbin/run.sh  
  
EXPOSE 5432  
CMD ["/usr/local/sbin/run.sh"]  

