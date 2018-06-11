FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="PostgreSQL database" \  
io.k8s.display-name="PostgreSQL"  
  
RUN rpm -ivh http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-1.noarch.rpm  
RUN yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y postgresql94 postgresql94-contrib postgresql94-server \  
postgresql94-devel python-psycopg2 pg_jobmon94 check_postgres \  
hostname bind-utils python-pip make gcc && \  
yum clean all -y && \  
pip install j2cli && \  
test "$(id postgres)" = "uid=26(postgres) gid=26(postgres)
groups=26(postgres)"  
  
RUN curl -Lo /tmp/pg_partman.tar.gz
https://github.com/keithf4/pg_partman/archive/v2.3.4.tar.gz && \  
tar -zxf /tmp/pg_partman.tar.gz -C /tmp && \  
cd /tmp/pg_partman-2.3.4 && \  
make PG_CONFIG=/usr/pgsql-9.4/bin/pg_config install && \  
rm -rf /tmp/pg_partman.tar.gz /tmp/pg_partman-2.3.4  
  
ADD files /  
ADD templates /tmp/templates  
RUN chmod 755 /usr/bin/run-postgresql && \  
mkdir -p /var/lib/pgsql/data && \  
chown -R 26:26 /etc/pgsql /var/lib/pgsql/data  
  
ENV MAX_CONNECTIONS=450  
USER 26  
EXPOSE 5432  
VOLUME /mnt/data  
CMD ["run-postgresql"]  

