FROM centos:centos6  
RUN rpm -ivh http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-
centos93-9.3-1.noarch.rpm  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y install postgresql93-server postgis2_93 postgresql93-devel
pgrouting_93  
RUN yum -y install leveldb-devel snappy-devel cmake gcc gcc-c++ expat-devel
boost-devel  
RUN service postgresql-9.3 initdb --locale=ja_JP.UTF-8 -E UTF-8  
ADD pg_dba.conf /var/lib/pgsql/9.3/data/pg_hba.conf  

