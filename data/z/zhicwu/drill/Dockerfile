#  
# This docker image is just for development and testing purpose - please do
NOT use on production  
#  
# Pull Base Image  
FROM zhicwu/java:7  
# Set Maintainer Details  
MAINTAINER Zhichun Wu <zhicwu@gmail.com>  
  
# Set Environment Variables  
ENV DRILL_VERSION=1.5.0 DRILL_HOME=/apache-drill \  
APACHE_BASE_URL=http://www.apache.org/dyn/closer.lua?action=download&filename=
\  
MAVEN_BASE_URL=http://central.maven.org/maven2 \  
MYSQL_DRIVER_VERSION=5.1.38 PRESTO_DRIVER_VERSION=0.138 JTDS_VERSION=1.3.1  
# Set labels  
LABEL drill_version="Apache Drill $DRILL_VERSION"  
  
# Install Apache Drill  
RUN wget ${APACHE_BASE_URL}/drill/drill-${DRILL_VERSION}/apache-
drill-${DRILL_VERSION}.tar.gz \  
${MAVEN_BASE_URL}/mysql/mysql-connector-java/${MYSQL_DRIVER_VERSION}/mysql-
connector-java-${MYSQL_DRIVER_VERSION}.jar \  
${MAVEN_BASE_URL}/com/facebook/presto/presto-
jdbc/${PRESTO_DRIVER_VERSION}/presto-jdbc-${PRESTO_DRIVER_VERSION}.jar \  
${MAVEN_BASE_URL}/net/sourceforge/jtds/jtds/${JTDS_VERSION}/jtds-${JTDS_VERSION}.jar
\  
&& tar zxvf *.tar.gz \  
&& rm -f *.tar.gz \  
&& ln -s apache-drill-${DRILL_VERSION} ${DRILL_HOME} \  
&& mv *.jar ${DRILL_HOME}/jars/3rdparty/.  
  
WORKDIR $DRILL_HOME  
  
COPY config-and-run.sh ./bin/  
  
RUN chmod +x ./bin/*.sh \  
&& sed -i -e 's/nohup \\(\$thiscmd .* 2>&1\\).*/\1/'
$DRILL_HOME/bin/drillbit.sh \  
&& sed -i -e 's/\\(\$command .* 2>&1\\).*/\1/' $DRILL_HOME/bin/drillbit.sh  
  
# http://drill.apache.org/docs/ports-used-by-drill/  
# 8047 - Needed for the Drill Web Console  
# 31010 - User port address  
# 31011 - Control port address  
# 31012 - Data port address  
# 46655 - Used for JGroups and Infinispan  
EXPOSE 8047 31010 31011 31022 46655  
VOLUME ["$DRILL_HOME/log"]  
  
CMD ["./bin/config-and-run.sh"]  

