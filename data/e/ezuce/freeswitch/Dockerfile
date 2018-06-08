FROM centos:6.8  
MAINTAINER Mihai <costache.mircea.mihai@gmail.com>  
  
ADD sipxcom.repo /etc/yum.repos.d/  
RUN yum install -y freeswitch* && rm -f /etc/yum.repos.d/sipxecs.repo && yum
clean all && rm -rf /var/cache/yum/x86_64/6/sipxecs  
  
VOLUME ["/etc/sipxpbx/freeswitch", "/var/sipxdata/tmp/freeswitch",
"/var/log/sipxpbx/freeswitch", "/var/run/sipxpbx/freeswitch"]  
  
EXPOSE 8084 8031 8021 15060 8184 8284  
EXPOSE 11000-12999  
CMD freeswitch -nonat -conf /etc/sipxpbx/freeswitch/conf -db
/var/sipxdata/tmp/freeswitch -log /var/log/sipxpbx/freeswitch -run
/var/run/sipxpbx -htdocs /etc/sipxpbx/freeswitch/conf/htdoc  

