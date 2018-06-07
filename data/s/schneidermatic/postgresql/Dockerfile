#==============================================================================  
# Ported by: Markus Schneider  
# Arch: x86_64  
# Entities: CentOS-7.2  
# PostgreSQL 9.5  
# Original Authors:  
#  
# "ported" by Adam Miller <maxamillion@fedoraproject.org> from  
# https://github.com/fedora-cloud/Fedora-Dockerfiles  
#  
# Originally written for Fedora-Dockerfiles by  
# scollier <scollier@redhat.com>  
#==============================================================================  
  
FROM schneidermatic/centos:centos-7.2  
MAINTAINER Markus Schneider <markus.schneider73@gmail.com>  
  
## Install PostgreSQL  
WORKDIR /tmp  
RUN wget
https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-
centos95-9.5-3.noarch.rpm  
RUN rpm -ivh ./pgdg-centos95-9.5-3.noarch.rpm  
RUN yum -y install postgresql95-server  
RUN yum -y install postgresql95  
RUN yum -y install postgresql95-contrib  
RUN yum clean all  
  
## Add Custom Scripts/Configs  
ADD ./src/config/supervisord.conf /etc/supervisord.conf  
ADD ./src/scripts/bootstrap.sh /opt/docker/scripts/bootstrap.sh  
ADD ./src/scripts/dbadmin.sh /opt/docker/scripts/dbadmin.sh  
  
## Sudo requires a tty. fix that.  
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers  
RUN chmod 775 /opt/docker/scripts/*.sh  
  
## Configure PostgreSQL  
RUN mkdir /var/lib/pgsql/9.5/log  
RUN chown -R postgres:postgres /var/lib/pgsql/9.5/log  
RUN chmod -R 700 /var/lib/pgsql/9.5/log  
RUN sudo -u postgres /usr/pgsql-9.5/bin/initdb -E UTF8 /var/lib/pgsql/9.5/data  
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/"
/var/lib/pgsql/9.5/data/postgresql.conf  
RUN sed -i "s/#port = 5432/port = 5432/"
/var/lib/pgsql/9.5/data/postgresql.conf  
RUN chown -v postgres:postgres /var/lib/pgsql/9.5/data/postgresql.conf  
RUN echo "host all all 0.0.0.0/0 trust" >> /var/lib/pgsql/9.5/data/pg_hba.conf  
  
VOLUME ["/var/lib/pgsql"]  
  
##------------------------------------------------------------------------------  
## EXPOSED PORTS  
##------------------------------------------------------------------------------  
## -- PostgreSQL Port(5432)  
EXPOSE 5432  
  
CMD ["/bin/bash", "/opt/docker/scripts/bootstrap.sh"]  

