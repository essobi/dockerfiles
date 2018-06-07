FROM tomcat:latest  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# To update, check http://guac-dev.org/releases  
ENV GUACAMOLE_VERSION 0.9.4  
ENV GUACAMOLE_WAR_SHA1 07d194593db296d20d87b858b02e7816fb4a9315  
ENV MYSQL_CONNECTOR_MD5 ad4c875c719247f8e8c41cd7f0609e00  
  
ENV DB_PASS wh4zUP  
  
  
### Guacamole webapp  
# Disable Tomcat's manager application.  
RUN rm -rf webapps/*  
  
# Fetch and install Guacamole war archive.  
RUN curl -L -o webapps/ROOT.war
http://sourceforge.net/projects/guacamole/files/current/binary/guacamole-${GUACAMOLE_VERSION}.war/download
&& \  
cd webapps  
  
# Expose tomcat runtime options through the RUNTIME_OPTS environment variable.  
# Example to set the JVM's max heap size to 256MB use the flag  
# '-e RUNTIME_OPTS="-Xmx256m"' when starting a container.  
RUN echo 'export CATALINA_OPTS="$RUNTIME_OPTS"' > bin/setenv.sh  
  
### Guacamole MySQL auth extension  
# Fetch and install Guacamole MySQL auth extension libs  
RUN mkdir -p /guacamole/classpath  
RUN curl -L -o guacamole-auth-mysql.tar.gz
http://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-
auth-mysql-0.9.4.tar.gz/download && \  
tar xzf guacamole-auth-mysql.tar.gz && \  
mv guacamole-auth-mysql-${GUACAMOLE_VERSION}/lib/*.jar /guacamole/classpath &&
\  
rm -rf guacamole-auth-mysql*  
  
# Fetch and install MySQL connector  
RUN curl -L -o mysql-connector.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.34.tar.gz && \  
tar xzf mysql-connector.tar.gz && \  
mv mysql-connector-java-*/mysql-connector-java-*.jar /guacamole/classpath && \  
rm -rf mysql-connector*  
  
# prepare and move  
#ADD ./conf/guacamole.properties /guacamole/  
#RUN echo "mysql-password: ${DB_PASS}" >> /guacamole/guacamole.properties  
COPY ./conf/guacamole.properties guacamole/  
  
ENV GUACAMOLE_HOME /guacamole  
  
# inherited run from parent will be called

