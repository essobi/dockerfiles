FROM pulsepointinc/centos6-java8:latest  
  
COPY ./cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo  
  
RUN \  
rpm --rebuilddb && \  
yum install -y \  
hadoop-client \  
hadoop-libhdfs \  
hive \  
hive-hbase \  
impala-shell \  
openssl-devel \  
spark-core \  
sqoop \  
sqoop2-client && \  
yum clean all  
  
ENV LD_LIBRARY_PATH=/usr/lib/hadoop/lib/native  

