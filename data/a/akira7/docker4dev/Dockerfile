FROM centos:6  
MAINTAINER Stanly Xiang <stanly.sxiang@gmail.com>  
  
USER root  
  
RUN yum -y install sudo  
  
RUN useradd postgres  
  
RUN chmod +w /etc/sudoers  
  
RUN echo "postgres ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN chmod -w /etc/sudoers  
  
RUN yum -y install
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-
centos96-9.6-3.noarch.rpm  
  
RUN yum -y groupinstall "PostgreSQL Database Server 9.6 PGDG"  
  
RUN ln -s /etc/rc.d/init.d/postgresql-9.6 /etc/rc.d/init.d/postgresql  
  
RUN chkconfig postgresql on  
  
USER postgres  
  
RUN sudo service postgresql initdb  
  
WORKDIR /home/postgres  

