FROM tomcat:9.0-jre8-alpine  
MAINTAINER Degenerate76  
  
# To update, check http://guacamole.apache.org/releases and
https://jdbc.postgresql.org/download.html  
ENV GUACAMOLE_VERSION 0.9.14  
ENV GUACAMOLE_WAR_SHA1
8831d9720a6a984919dd00f683c114136f35e0f07b33df171714026ecb23d94d  
ENV GUACAMOLE_AUTH_JDBC_SHA1
c7f744fa2fe9644b6a3ea4e4e5c59a33e7603e0eb3610fc27018ed9552a4a476  
ENV POSTGRES_CONNECTOR_VERSION 42.2.1  
ENV POSTGRES_CONNECTOR_SHA1 b7f61848ac43ae9fa6e38935bfd75628b7fc9086  
  
RUN apk add --update curl  
### Guacamole webapp  
# Disable Tomcat's manager application.  
RUN rm -rf webapps/*  
  
# Fetch and install Guacamole war archive.  
RUN echo $GUACAMOLE_WAR_SHA1 ROOT.war > webapps/ROOT.war.sha1 && \  
curl -L -o webapps/ROOT.war
https://www.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/binary/guacamole-${GUACAMOLE_VERSION}.war
&& \  
cd webapps && sha1sum ROOT.war.sha1 | cut -d " " -f 1  
  
# Expose tomcat runtime options through the RUNTIME_OPTS environment variable.  
# Example to set the JVM's max heap size to 256MB use the flag  
# '-e RUNTIME_OPTS="-Xmx256m"' when starting a container.  
RUN echo 'export CATALINA_OPTS="$RUNTIME_OPTS"' > bin/setenv.sh  
  
### Guacamole Postgres auth extension  
# Fetch and install Guacamole JDBC auth extension libs  
RUN mkdir -p /guacamole/extensions && \  
mkdir -p /guacamole/lib && \  
mkdir -p /guacamole/bin  
RUN echo $GUACAMOLE_AUTH_JDBC_SHA1 guacamole-auth-jdbc.tar.gz > guacamole-
auth-jdbc.tar.gz.sha1 && \  
curl -L -o guacamole-auth-jdbc.tar.gz
https://www.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/binary/guacamole-
auth-jdbc-${GUACAMOLE_VERSION}.tar.gz && \  
sha1sum guacamole-auth-jdbc.tar.gz.sha1 | cut -d " " -f 1 && \  
tar xzf guacamole-auth-jdbc.tar.gz && \  
mv guacamole-auth-jdbc-${GUACAMOLE_VERSION}/postgresql/*.jar
/guacamole/extensions && \  
rm -rf guacamole-auth-jdbc*  
  
# Fetch and install Postgres connector  
RUN echo $POSTGRES_CONNECTOR_SHA1 postgres-connector.jar > postgres-
connector.jar.sha1 && \  
curl -L -o postgres-connector.jar
https://jdbc.postgresql.org/download/postgresql-${POSTGRES_CONNECTOR_VERSION}.jar
&& \  
sha1sum postgres-connector.jar.sha1 | cut -d " " -f 1 && \  
mv postgres-connector.jar /guacamole/lib  
  
### Configuration  
ENV GUACAMOLE_HOME /guacamole  
COPY start.sh ${GUACAMOLE_HOME}/bin/  
RUN chmod 544 ${GUACAMOLE_HOME}/bin/start.sh  
EXPOSE 8080  
CMD ["/guacamole/bin/start.sh"]  

