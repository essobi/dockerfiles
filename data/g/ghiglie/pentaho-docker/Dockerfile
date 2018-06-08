FROM openjdk:8-jre-alpine  
ENV MAJOR_VERSION 7.1  
ENV MINOR_VERSION 7.1.0.0-12  
ENV PENTAHO_HOME /opt/pentaho  
ENV PENTAHO_JAVA_HOME $JAVA_HOME  
ENV PENTAHO_SERVER ${PENTAHO_HOME}/pentaho-server  
ENV CATALINA_OPTS="-Djava.awt.headless=true -Xms4096m -Xmx6144m
-XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000
-Dsun.rmi.dgc.server.gcInterval=3600000"  
# Get support packages  
RUN apk add --update wget \  
unzip \  
bash \  
xvfb \  
postgresql-client \  
ttf-dejavu  
  
# Setup pentaho user  
RUN mkdir -p ${PENTAHO_HOME}/.pentaho ${PENTAHO_HOME}/scripts; \  
adduser -D -s /bin/sh -h ${PENTAHO_HOME} pentaho; \  
chown -R pentaho:pentaho ${PENTAHO_HOME}; \  
chmod -R +x ${PENTAHO_HOME}/scripts  
USER pentaho  
WORKDIR ${PENTAHO_HOME}  
  
# Get Pentaho Server  
RUN echo
http://downloads.sourceforge.net/project/pentaho/Business%20Intelligence%20Server/${MAJOR_VERSION}/pentaho-
server-ce-${MINOR_VERSION}.zip | xargs wget -qO- -O tmp.zip && \  
unzip -q tmp.zip -d . && \  
rm -f tmp.zip  
  
# Get MS SQL JDBC driver  
RUN echo
https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/enu/sqljdbc_6.0.8112.100_enu.tar.gz
| xargs wget -qO- -O tmp.tar.gz && \  
tar -zxf tmp.tar.gz && \  
rm -f tmp.tar.gz && \  
cp sqljdbc_6.0/enu/jre8/sqljdbc42.jar ${PENTAHO_SERVER}/tomcat/lib/ && \  
rm -fr sqljdbc_6.0  
  
# Replace outdated Postgresql JDBC driver  
RUN rm ${PENTAHO_SERVER}/tomcat/lib/postgresql-9.3-1102-jdbc4.jar && \  
echo https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar | xargs wget
-qO- -O ${PENTAHO_SERVER}/tomcat/lib/postgresql-9.4.1212.jar  
  
# Disable first-time startup prompt  
RUN rm ${PENTAHO_SERVER}/promptuser.sh  
  
# Disable daemon mode for Tomcat  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/'
${PENTAHO_SERVER}/tomcat/bin/startup.sh  
  
# Volumes:  
# Administration and user accounts:  
# /opt/pentaho/server/pentaho-server/data/hsqldb  
# Jackrabbit document repository:  
# /opt/pentaho/server/pentaho-server/pentaho-
solutions/system/jackrabbit/repository  
VOLUME [ '/opt/pentaho/server/pentaho-server/data/hsqldb',
'/opt/pentaho/server/pentaho-server/pentaho-
solutions/system/jackrabbit/repository' ]  
  
EXPOSE 8080  
ENTRYPOINT ["sh", "-c", "$PENTAHO_HOME/scripts/run.sh"]  

