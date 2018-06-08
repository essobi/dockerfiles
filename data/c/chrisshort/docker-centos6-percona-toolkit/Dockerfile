FROM centos:centos6  
MAINTAINER Chris Short <chris@chrisshort.net>  
  
RUN yum -y update && yum clean all  
RUN yum -y install wget perl perl-libs perl-DBI perl-DBD-MySQL perl-Time-HiRes
perl-IO-Socket-SSL perl-Crypt-PasswdMD5 perl-TermReadKey && yum clean all  
RUN rm -rf /usr/share/doc/* && rm -rf /usr/share/info/* && rm -rf /tmp/* && rm
-rf /var/tmp/*  
  
WORKDIR /tmp  
RUN wget percona.com/get/percona-toolkit.rpm && rpm -iv percona-toolkit.rpm &&
rm -f percona-toolkit.rpm  
  
WORKDIR /  

