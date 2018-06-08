FROM centos:centos6  
MAINTAINER Yasushi YAMAZAKI  
  
# convert into Oracle Linux 6  
RUN curl -O https://linux.oracle.com/switch/centos2ol.sh  
RUN sh centos2ol.sh; echo success  
  
# fix missing MAKEDEV error  
RUN yum install -y MAKEDEV  
RUN yum upgrade -y  
  
# fix locale error  
RUN yum reinstall -y glibc-common  
RUN echo LANG=en_US.utf-8 >> /etc/environment \  
&& echo LC_ALL=en_US.utf-8 >> /etc/environment  
  
# add extra packages  
RUN yum install -y vim-minimal  
RUN yum install -y oracle-rdbms-server-12cR1-preinstall  
  
# create directories  
RUN mkdir /opt/oracle /opt/oraInventory /opt/datafile \  
&& chown oracle:oinstall -R /opt  
  
# set environment variables  
RUN echo "export ORACLE_BASE=/opt/oracle" >> /home/oracle/.bash_profile \  
&& echo "export ORACLE_HOME=/opt/oracle/product/12.1.0.2/dbhome_1" >>
/home/oracle/.bash_profile \  
&& echo "export ORACLE_SID=orcl" >> /home/oracle/.bash_profile \  
&& echo "export PATH=\$PATH:\$ORACLE_HOME/bin" >> /home/oracle/.bash_profile  
  
# confirm  
RUN cat /etc/oracle-release  

