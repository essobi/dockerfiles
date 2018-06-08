FROM chenmins/tomcat-centos:jdk7tomcat7  
MAINTAINER Chenmin  
  
ENV TOMCAT_HOME=/opt/tomcat \  
JAVA_HOME=/usr/java/jdk1.7.0_80 \  
JDBC_HOME=jdbc \  
APP_HOME=app  
  
ADD ${JDBC_HOME}/*.jar ${TOMCAT_HOME}/lib/  
COPY ${APP_HOME}/* ${TOMCAT_HOME}/webapps/  
RUN cat ${TOMCAT_HOME}/webapps/default.s* >
${TOMCAT_HOME}/webapps/default.tar.gz && \  
cat ${TOMCAT_HOME}/webapps/governor.s* >
${TOMCAT_HOME}/webapps/governor.tar.gz && \  
rm ${TOMCAT_HOME}/webapps/*.s* && \  
tar -xzvf ${TOMCAT_HOME}/webapps/default.tar.gz -C ${TOMCAT_HOME}/webapps/ &&
\  
tar -xzvf ${TOMCAT_HOME}/webapps/governor.tar.gz -C ${TOMCAT_HOME}/webapps/ &&
\  
rm ${TOMCAT_HOME}/webapps/*.gz  
  
ADD run.sh /opt  
ADD startServer.sh /opt  
ADD stopServer.sh /opt  
RUN chmod 755 /opt/*.sh  
RUN mkdir /opt/apps_config  
VOLUME ["/opt/apps_config"]  
  
EXPOSE 8080  
CMD ["/opt/run.sh"]

