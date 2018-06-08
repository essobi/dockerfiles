# "ported" by Adam Miller <maxamillion@fedoraproject.org> from  
# https://github.com/fedora-cloud/Fedora-Dockerfiles  
#  
# Originally written for Fedora-Dockerfiles by  
# scollier <scollier@redhat.com>  
FROM centos:centos6  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
RUN yum install -y
https://download.postgresql.org/pub/repos/yum/9.0/redhat/rhel-6-x86_64/pgdg-
centos90-9.0-5.noarch.rpm  
ADD ./CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install postgresql90-server postgresql90 postgresql90-contrib
supervisor; yum clean all  
  
ADD ./postgresql-setup /usr/bin/postgresql-setup  
ADD ./postgres_user.sh /postgres_user.sh  
ADD ./supervisord.conf /etc/supervisord.conf  
ADD ./start_postgres.sh /start_postgres.sh  
  
RUN chmod +x /usr/bin/postgresql-setup  
RUN chmod +x /start_postgres.sh  
RUN chmod +x /postgres_user.sh  
  
RUN /usr/bin/postgresql-setup initdb  
  
ADD ./postgresql.conf /var/lib/pgsql/data/postgresql.conf  
  
RUN chown -v postgres.postgres /var/lib/pgsql/data/postgresql.conf  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/pgsql/data/pg_hba.conf  
  
RUN /postgres_user.sh  
  
EXPOSE 5432  
CMD ["/bin/bash", "/start_postgres.sh"]  

