# https://www.percona.com/doc/percona-
xtrabackup/LATEST/installation/yum_repo.html  
FROM centos:7  
MAINTAINER Vitaly Uvarov <vitalyu@gmail.com>  
RUN yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm  
RUN yum -y install percona-xtrabackup-24  
ENTRYPOINT ["innobackupex"]

