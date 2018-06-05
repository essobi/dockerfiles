FROM centos:6  
RUN yum install -y gcc gcc-c++ make gperf boost-devel libevent-devel libuuid-
devel mysql-devel && \  
yum clean all  
  
ENV GEARMAN_VERSION "1.1.16"  
ENV MYSQL_TABLE=${MYSQL_TABLE:-gearman_queue}  
  
RUN curl -L
https://github.com/gearman/gearmand/releases/download/${GEARMAN_VERSION}/gearmand-${GEARMAN_VERSION}.tar.gz
\  
-o gearmand-${GEARMAN_VERSION}.tar.gz && \  
tar -zxf gearmand-${GEARMAN_VERSION}.tar.gz  
  
RUN cd ./gearmand-${GEARMAN_VERSION} && \  
./configure && \  
make && \  
make install  
  
EXPOSE 4730  
CMD gearmand \  
\--log-file=/var/log/gearmand.log \  
\--queue-type=mysql \  
\--mysql-host=${MYSQL_HOST} \  
\--mysql-user=${MYSQL_USER} \  
\--mysql-password=${MYSQL_PASSWORD} \  
\--mysql-db=${MYSQL_DB} \  
\--mysql-table=${MYSQL_TABLE} \  
\--mysql-port=3306

