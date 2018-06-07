FROM ticksmith/impala-base:2.9.0  
ENV HIVE_RELEASE=hive-2.1.0  
RUN mkdir -p /opt/ && wget --continue
http://archive.apache.org/dist/hive/${HIVE_RELEASE}/apache-${HIVE_RELEASE}-bin.tar.gz
-O /opt/${HIVE_RELEASE}.tar.gz && cd /opt/ && tar xvzf ${HIVE_RELEASE}.tar.gz
&& ln -sf /opt/apache-${HIVE_RELEASE}-bin /opt/hive && rm
/opt/${HIVE_RELEASE}.tar.gz && rm /opt/hive/lib/log4j-slf4j-impl-*.jar && wget
--continue http://central.maven.org/maven2/org/mariadb/jdbc/mariadb-java-
client/1.1.7/mariadb-java-client-1.1.7.jar -O /opt/hive/lib/mariadb-java-
client-1.1.7.jar && yum install -y mariadb  
ADD waitfor.sh /usr/bin/waitfor.sh  
ADD start.sh /usr/bin/start.sh  
COPY conf_template/* /etc/hadoop/conf.template/  
CMD ["/usr/bin/start.sh"]  
  

