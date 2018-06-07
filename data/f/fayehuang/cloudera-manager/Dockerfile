FROM fayehuang/centos-serf  
MAINTAINER FayeHuang  
#  
WORKDIR /docker_init/cm  
RUN mkdir cm  
#  
ENV mysql_password=changeme  
RUN yum install -y ntp mysql-server mysql-connector-java && yum clean all  
RUN pip install cm_api  
RUN echo -e "\nY\n$mysql_password\n$mysql_password\nY\nn\nY\nY\n" >
mysql_secure_install_answer  
#  
ENV cm_version=5.4.3 cdh_version=5.4.4  
RUN wget http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-
cdh5.repo && mv cloudera-cdh5.repo /etc/yum.repos.d && \  
wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo
&& mv cloudera-manager.repo /etc/yum.repos.d && \  
sed -i.bak
s/^.*"baseurl".*/"baseurl=http:\/\/archive.cloudera.com\/cdh5\/redhat\/6\/x86_64\/cdh\/$cdh_version\/"/
/etc/yum.repos.d/cloudera-cdh5.repo && \  
sed -i.bak
s/^.*"baseurl".*/"baseurl=http:\/\/archive.cloudera.com\/cm5\/redhat\/6\/x86_64\/cm\/$cm_version\/"/
/etc/yum.repos.d/cloudera-manager.repo  
  
RUN yum install -y hive && yum clean all  
RUN ln -s /usr/share/java/mysql-connector-java.jar /usr/lib/hive/lib/mysql-
connector-java.jar  
# fixed "Failed to open file 'hive-txn-schema-0.13.0.mysql.sql', error: 2"  
RUN sed -i.bak s/^.*"hive-txn-schema-0.13.0.mysql.sql".*/"SOURCE
\/usr\/lib\/hive\/scripts\/metastore\/upgrade\/mysql\/hive-txn-
schema-0.13.0.mysql.sql;"/ /usr/lib/hive/scripts/metastore/upgrade/mysql/hive-
schema-1.1.0.mysql.sql  
#  
RUN yum install -y cloudera-manager-agent cloudera-manager-daemons cloudera-
manager-server cloudera-manager-server-db-2 && yum clean all  
COPY cm_init.sh cm_init.sh  
RUN chmod +x cm_init.sh  
ENV SERF_HOME /docker_init/serf  
COPY serf_init.sh $SERF_HOME/bin/serf_init.sh  
RUN chmod +x $SERF_HOME/bin/serf_init.sh  
COPY deployCDH.py deployCDH.py  
  
COPY supervisord.conf /etc/supervisord.conf  
EXPOSE 22 7180 3000  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

