FROM centos:6  
# using epel  
#RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-
release-5-4.noarch.rpm  
#RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/5Server/x86_64/epel-
release-5-4.noarch.rpm  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# update / install  
RUN yum -y update  
RUN yum -y install mysql mysql-devel mysqlclient mysqlreport perl-DBD-MySQL
expat-devel openssl openssl-devel initscripts unixODBC unixODBC-devel
postgresql-libs  
  
#RUN rpm -Uvh http://sphinxsearch.com/files/sphinx-2.0.4-1.rhel5.x86_64.rpm  
RUN rpm -Uhv http://sphinxsearch.com/files/sphinx-2.2.11-2.rhel6.x86_64.rpm  
RUN yum -y install sphinx  
  
RUN mkdir /var/lib/sphinx/data  
RUN chown -R sphinx:sphinx /var/lib/sphinx  
  
ADD run.sh /  
RUN chmod 755 /run.sh  
  
CMD /run.sh  
  
# libcrypto.so.6()(64bit) is needed by sphinx-2.0.4-1.rhel5.x86_64  
# libexpat.so.0()(64bit) is needed by sphinx-2.0.4-1.rhel5.x86_64  
# libmysqlclient.so.15()(64bit) is needed by sphinx-2.0.4-1.rhel5.x86_64  
# libmysqlclient.so.15(libmysqlclient_15)(64bit) is needed by
sphinx-2.0.4-1.rhel5.x86_64  
# libssl.so.6()(64bit) is needed by sphinx-2.0.4-1.rhel5.x86_64  

