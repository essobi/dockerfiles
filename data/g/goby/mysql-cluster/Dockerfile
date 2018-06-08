FROM debian:wheezy-slim  
  
MAINTAINER goby goby@foxmail.com  
  
ENV MYSQL_USER mysql  
ENV MYSQL_GROUP mysql  
  
ENV MYSQL_CLUSTER_VERSION 7.5  
ENV MYSQL_CLUSTER_MINOR_VERSION 6  
ENV MYSQL_CLUSTER_HOME /usr/local/mysql  
ENV MYSQL_CLUSTER_LOG ${MYSQL_CLUSTER_HOME}/log  
ENV MYSQL_CLUSTER_DATA ${MYSQL_CLUSTER_HOME}/data  
ENV MYSQL_CLUSTER_CONFIG /etc/mysql-cluster.ini  
  
ENV KUBECTL_VERSION 1.6.1  
ENV PATH ${PATH}:${MYSQL_CLUSTER_HOME}/bin  
  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list \  
&& apt-get update && apt-get install -y libaio1 curl jq \  
&& groupadd ${MYSQL_GROUP} && useradd -g ${MYSQL_GROUP} ${MYSQL_USER} \  
&& mkdir -p ${MYSQL_CLUSTER_HOME} ${MYSQL_CLUSTER_DATA} ${MYSQL_CLUSTER_LOG} \  
&& curl -sL https://dev.mysql.com/get/Downloads/MySQL-
Cluster-${MYSQL_CLUSTER_VERSION}/mysql-cluster-
gpl-${MYSQL_CLUSTER_VERSION}.${MYSQL_CLUSTER_MINOR_VERSION}-linux-
glibc2.5-x86_64.tar.gz | tar --strip=1 -C ${MYSQL_CLUSTER_HOME} -xz \  
&& chown -R ${MYSQL_USER}:${MYSQL_GROUP} ${MYSQL_CLUSTER_DATA} \  
&& chgrp -R ${MYSQL_GROUP} ${MYSQL_CLUSTER_HOME} \  
&& rm -fr ${MYSQL_CLUSTER_HOME}/lib \  
&& rm -fr ${MYSQL_CLUSTER_HOME}/mysql-test \  
&& cd ${MYSQL_CLUSTER_HOME}/bin && find . ! -name mysql ! -name ndbd ! -name
mysqld ! -name mysqld_safe ! -name ndb_mgm ! -name ndb_mgmd -delete  
# && ${MYSQL_CLUSTER_HOME}/bin/mysqld --initialize-insecure
--user=${MYSQL_USER} --datadir=${MYSQL_CLUSTER_DATA}  
VOLUME ${MYSQL_CLUSTER_LOG}  
VOLUME ${MYSQL_CLUSTER_DATA}  
  
WORKDIR ${MYSQL_CLUSTER_HOME}  
  
EXPOSE 1186 3306  
ADD run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

