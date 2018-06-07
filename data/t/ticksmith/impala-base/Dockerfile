FROM centos:7  
RUN yum update -y && yum install -y java-1.8.0-openjdk wget epel-release &&
yum repolist && yum install -y python-pip && pip install awscli && wget
https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/cloudera-cdh5.repo -O
/etc/yum.repos.d/cloudera-cdh5.repo && yum clean all && yum repolist && yum
install -y impala-server impala-catalog impala-state-store impala-shell  
ADD entrypoint.sh /entrypoint.sh  
ADD start_impalad.sh /usr/bin/start_impalad.sh  
ADD start_catalogd.sh /usr/bin/start_catalogd.sh  
ADD start_statestored.sh /usr/bin/start_statestored.sh  
ADD wait_metastore.sh /usr/bin/wait_metastore.sh  
ADD hdfs-site.xml /etc/hadoop/conf.template/  
ADD hive-site.xml /etc/hadoop/conf.template/  
ADD impala.conf.template /etc/impala/impala.conf.template  
ENTRYPOINT ["/entrypoint.sh"]  
  

