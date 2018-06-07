FROM hegand/hadoop-base:2.7  
  
ENV HIVE_VERSION 2.1.1  
ENV HIVE_FULL_VERSION hive-${HIVE_VERSION}  
ENV HIVE_HOME /usr/local/hive  
ENV HCAT_HOME ${HIVE_HOME}/hcatalog  
  
ENV SQOOP_VERSION 1.4.6  
ENV SQOOP_FULL_VERSION sqoop-${SQOOP_VERSION}  
ENV SQOOP_HOME /usr/local/sqoop  
  
ENV PATH $PATH:$HIVE_HOME/bin:$SQOOP_HOME/bin:${HCAT_HOME}/bin  
  
RUN set -x \  
&& adduser -D -s /bin/bash -u 1110 yarn \  
&& adduser -D -s /bin/bash -u 1120 mapred \  
&& adduser -D -s /bin/bash -u 1130 hive \  
&& adduser -D -s /bin/bash -u 1140 sqoop  
  
RUN set -x \  
&& cd /tmp \  
&& wget
http://apache.claz.org/hive/${HIVE_FULL_VERSION}/apache-${HIVE_FULL_VERSION}-bin.tar.gz
-O - | tar -xz \  
&& mv apache-${HIVE_FULL_VERSION}-bin /usr/local \  
&& ln -s /usr/local/apache-${HIVE_FULL_VERSION}-bin ${HIVE_HOME} \  
&& rm -rf ${HIVE_HOME}/examples \  
&& chown -R hive:hive ${HIVE_HOME}/  
  
RUN set -x \  
&& cd /tmp \  
&& wget
http://apache.claz.org/sqoop/${SQOOP_VERSION}/${SQOOP_FULL_VERSION}.bin__hadoop-2.0.4-alpha.tar.gz
-O - | tar -xz \  
&& mv ${SQOOP_FULL_VERSION}.bin__hadoop-2.0.4-alpha /usr/local \  
&& mv /usr/local/${SQOOP_FULL_VERSION}.bin__hadoop-2.0.4-alpha
/usr/local/${SQOOP_FULL_VERSION} \  
&& ln -s /usr/local/${SQOOP_FULL_VERSION} ${SQOOP_HOME} \  
&& rm -rf ${SQOOP_HOME}/{docs,ivy,src,testdata,sqoop-test-1.4.6.jar} \  
&& chown -R sqoop:sqoop ${SQOOP_HOME}/  
  
RUN set -x \  
&& mkdir -p /usr/share/java \  
&& cd /usr/share/java \  
&& wget https://jdbc.postgresql.org/download/postgresql-42.0.0.jar \  
&& wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.41.tar.gz -O - | tar -xz \  
&& mv mysql-connector-java-5.1.41/mysql-connector-java-5.1.41-bin.jar ./ \  
&& rm -rf mysql-connector-java-5.1.41 \  
&& ln -s /usr/share/java/postgresql-42.0.0.jar
${HIVE_HOME}/lib/postgresql-42.0.0.jar \  
&& ln -s /usr/share/java/mysql-connector-java-5.1.41-bin.jar
${HIVE_HOME}/lib/mysql-connector-java-5.1.41-bin.jar \  
&& ln -s /usr/share/java/postgresql-42.0.0.jar
${SQOOP_HOME}/lib/postgresql-42.0.0.jar \  
&& ln -s /usr/share/java/mysql-connector-java-5.1.41-bin.jar
${SQOOP_HOME}/lib/mysql-connector-java-5.1.41-bin.jar  
  
WORKDIR ${HADOOP_HOME}  

