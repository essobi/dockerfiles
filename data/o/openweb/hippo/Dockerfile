#docker build -f Dockerfile -t openweb/hippo:mysql-10 .  
FROM openweb/oracle-tomcat:8-jre8  
MAINTAINER Ebrahim Aharpour <ebrahim@openweb.nl>  
  
ENV ENCODING=UTF-8 \  
CATALINA_HOME=/usr/local/tomcat \  
\  
MAX_HEAP=512 \  
MIN_HEAP=256 \  
EXTRA_OPTS="" \  
\  
RMI_SERVER_HOSTNAME=127.0.0.1 \  
\  
MAIL_SESSION_RESOURCE_NAME=mail/Session \  
MAIL_USERNAME="" \  
MAIL_PASSWORD="" \  
MAIL_HOST=localhost \  
MAIL_DEBUG=false \  
MAIL_PROTOCOL=smtp \  
MAIL_AUTH=true \  
MAIL_PORT=25 \  
MAIL_FROM="" \  
MAIL_TLS_ENABLE=true \  
\  
DB_RESOURCE_NAME=jdbc/repositoryDS \  
DB_HOST="" \  
DB_PORT=3306 \  
DB_NAME=hippo \  
DB_USER=hippo \  
DB_PASS="" \  
\  
MYSQL_CONNECTOR_VERSION=5.1.38 \  
\  
REPO_BOOTSTRAP=true \  
CONSISTENCY_CHECK=none  
  
WORKDIR $CATALINA_HOME  
  
COPY ["bin/setenv.sh", \  
"bin/wait-for-it.sh", \  
"bin/entrypoint.sh", \  
"$CATALINA_HOME/bin/"]  
  
COPY ["conf/repository.xml", \  
"conf/repository-consistency.xml", \  
"conf/repository-force.xml", \  
"conf/context.xml.template", \  
"conf/server.xml", \  
"conf/catalina.properties", \  
"conf/catalina.policy", \  
"conf/log4j.xml", \  
"$CATALINA_HOME/conf/"]  
  
RUN rm -rf $CATALINA_HOME/webapps/* &&\  
mkdir -p $CATALINA_HOME/endorsed &&\  
curl -s -o $CATALINA_HOME/endorsed/mysql-connector-
java-$MYSQL_CONNECTOR_VERSION.jar -L
https://repo1.maven.org/maven2/mysql/mysql-connector-
java/$MYSQL_CONNECTOR_VERSION/mysql-connector-
java-$MYSQL_CONNECTOR_VERSION.jar &&\  
chmod +x $CATALINA_HOME/bin/setenv.sh &&\  
chmod +x bin/wait-for-it.sh &&\  
chmod +x bin/entrypoint.sh  
  
EXPOSE 1099  
  
VOLUME ["/usr/local/repository/", "/usr/local/tomcat/logs"]  
ENTRYPOINT ["bin/entrypoint.sh"]  
CMD ["/bin/bash", "catalina.sh", "run"]

