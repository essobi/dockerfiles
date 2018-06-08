FROM logicify/centos7  
MAINTAINER Dmitry Berezovsky <dmitry.berezovsky@logicify.net>  
  
RUN curl -o pgdg-centos.rpm
https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-2.noarch.rpm && rpm -ivf pgdg-centos.rpm && rm pgdg-centos.rpm  
RUN yum install -y pgbouncer  
  
ENV PG_MAX_CLIENT_CONN 500  
ENV PG_DEFAULT_POOL_SIZE 200  
ENV PG_SERVER_IDLE_TIMEOUT 500  
ADD run.sh /usr/local/bin/run-pgbouncer  
  
RUN chmod +x /usr/local/bin/run-pgbouncer \  
&& mkdir -p /var/run/postgresql/ \  
&& chown app:app /var/run/postgresql  
EXPOSE 6432  
CMD ["/usr/local/bin/run-pgbouncer"]  

