FROM parrotstream/centos-openjdk  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
USER root  
  
ADD cloudera-cdh5.repo /etc/yum.repos.d/  
RUN rpm --import https://archive.cloudera.com/cdh5/redhat/5/x86_64/cdh/RPM-
GPG-KEY-cloudera  
RUN yum install -y hbase-master hbase-regionserver hbase-rest hbase-thrift  
RUN yum clean all  
  
RUN groupadd supergroup; \  
usermod -a -G supergroup hbase; \  
rm /etc/security/limits.d/hbase.conf  
  
ADD etc/supervisord.conf /etc/  
ADD etc/hbase/conf/hbase-site.xml /etc/hbase/conf/  
  
WORKDIR /  
  
# Various helper scripts  
ADD bin/start-hbase.sh /  
ADD bin/supervisord-bootstrap.sh /  
ADD bin/wait-for-it.sh /  
RUN chmod +x /*.sh  
  
EXPOSE 8080 8085 9090 9095 60000 60010 60020 60030  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

