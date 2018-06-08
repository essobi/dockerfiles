FROM centos:7  
MAINTAINER Eduardo Gonzalez Gutierrez <dabarren@gmail.com>  
  
COPY jpackage-generic.repo /etc/yum.repos.d/jpackage-generic.repo  
  
RUN yum install -y
http://yum.spacewalkproject.org/2.5/RHEL/7/x86_64/spacewalk-
repo-2.5-3.el7.noarch.rpm \  
epel-release && \  
yum clean all  
  
RUN rpm --import http://www.jpackage.org/jpackage.asc && \  
rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 && \  
rpm --import http://yum.spacewalkproject.org/RPM-GPG-KEY-spacewalk-2015 && \  
yum clean all  
  
RUN yum -y install \  
spacewalk-setup-postgresql \  
spacewalk-postgresql \  
supervisor \  
yum clean all  
  
COPY answerfile.txt /tmp/answerfile.txt  
  
EXPOSE 80 443 5222 68 69  
USER postgres  
RUN /usr/bin/pg_ctl initdb -D /var/lib/pgsql/data/  
RUN /usr/bin/pg_ctl start -D /var/lib/pgsql/data/ -w -t 300 && \  
psql -c 'CREATE DATABASE spaceschema' && \  
psql -c "CREATE USER spaceuser WITH PASSWORD 'spacepw'" && \  
psql -c 'ALTER ROLE spaceuser SUPERUSER' && \  
createlang pltclu spaceschema  
  
USER root  
  
RUN su -c "/usr/bin/pg_ctl start -D /var/lib/pgsql/data/ -w -t 300" postgres
&& \  
su -c "spacewalk-setup --answer-file=/tmp/answerfile.txt --skip-db-diskspace-
check --skip-db-install" root ; exit 0  
  
ADD supervisord.conf /etc/supervisord.d/supervisord.conf  
  
ENTRYPOINT supervisord -c /etc/supervisord.d/supervisord.conf  

