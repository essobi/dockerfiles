FROM centos:centos6  
MAINTAINER Ganesh Ravi "ganesh.reddy.22@gmail.com"  
RUN rpm -Uvh http://yum.pgrpms.org/reporpms/8.4/pgdg-centos-8.4-2.noarch.rpm  
  
RUN yum -y install postgresql84-server postgresql84-contrib postgresql84  
  
RUN yum -y install sudo  
  
# tty is required for 'sudo'  
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers  
  
RUN /etc/init.d/postgresql-8.4 initdb  
  
ADD postgresql.conf /var/lib/pgsql/8.4/data/postgresql.conf  
  
ADD pg_hba.conf /var/lib/pgsql/8.4/data/pg_hba.conf  
  
RUN chown postgres:postgres /var/lib/pgsql/8.4/data/*.conf  
  
ADD run /usr/local/bin/run  
  
RUN chmod +x /usr/local/bin/run  
  
RUN mkdir -p /var/run/postgresql  
  
RUN chown -R postgres:postgres /var/run/postgresql/  
  
ENV TERM xterm  
  
VOLUME ["/var/lib/psql"]  
  
EXPOSE 5432  
CMD ["/usr/local/bin/run"]  

