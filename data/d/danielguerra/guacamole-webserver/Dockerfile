FROM tomcat:9.0-jre8-alpine  
MAINTAINER Daniel Guerra  
  
# To update, check http://guac-dev.org/releases  
ENV GUACAMOLE_VERSION 0.9.9  
ENV GUACAMOLE_WAR_SHA1 0ba2ff114ac4221794b148ab0e83370dbc6259c5  
ENV GUACAMOLE_AUTH_JDBC_SHA1 a09558e46329e3f09ca30783d2e3008c11aae43b  
ENV MYSQL_CONNECTOR_MD5 c8988d4fc6e44364a2f51efe5b5139c1  
  
RUN apk add --update curl  
### Guacamole webapp  
# Disable Tomcat's manager application.  
RUN rm -rf webapps/*  
  
# Fetch and install Guacamole war archive.  
RUN echo $GUACAMOLE_WAR_SHA1 ROOT.war > webapps/ROOT.war.sha1 && \  
curl -L -o webapps/ROOT.war
http://sourceforge.net/projects/guacamole/files/current/binary/guacamole-${GUACAMOLE_VERSION}.war/download
&& \  
cd webapps && sha1sum ROOT.war.sha1 | cut -d " " -f 1  
  
# Expose tomcat runtime options through the RUNTIME_OPTS environment variable.  
# Example to set the JVM's max heap size to 256MB use the flag  
# '-e RUNTIME_OPTS="-Xmx256m"' when starting a container.  
RUN echo 'export CATALINA_OPTS="$RUNTIME_OPTS"' > bin/setenv.sh  
  
### Guacamole MySQL auth extension  
# Fetch and install Guacamole JDBC auth extension libs  
RUN mkdir -p /guacamole/classpath  
RUN echo $GUACAMOLE_AUTH_JDBC_SHA1 guacamole-auth-jdbc.tar.gz > guacamole-
auth-jdbc.tar.gz.sha1 && \  
curl -L -o guacamole-auth-jdbc.tar.gz
http://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-
auth-jdbc-${GUACAMOLE_VERSION}.tar.gz/download && \  
sha1sum guacamole-auth-jdbc.tar.gz.sha1 | cut -d " " -f 1 && \  
tar xzf guacamole-auth-jdbc.tar.gz && \  
mv guacamole-auth-jdbc-${GUACAMOLE_VERSION}/mysql/*.jar /guacamole/classpath
&& \  
rm -rf guacamole-auth-jdbc*  
  
# Fetch and install MySQL connector  
RUN echo $MYSQL_CONNECTOR_MD5 mysql-connector.tar.gz > mysql-
connector.tar.gz.md5 && \  
curl -L -o mysql-connector.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.39.tar.gz && \  
md5sum mysql-connector.tar.gz.md5 | cut -d " " -f 1 && \  
tar xzf mysql-connector.tar.gz && \  
mv mysql-connector-java-*/mysql-connector-java-*.jar /guacamole/classpath && \  
rm -rf mysql-connector*  
  
### Configuration  
ENV GUACAMOLE_HOME /guacamole  
COPY guacamole.properties ${GUACAMOLE_HOME}/  
EXPOSE 8080  

