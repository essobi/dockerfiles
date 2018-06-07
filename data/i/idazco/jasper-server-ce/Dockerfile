FROM tomcat:7  
# Download zip file and decompress into /usr/src  
# TODO: Allow changing version, but keep in mind the .properties file is
related to the version  
RUN \  
curl -SL
http://sourceforge.net/projects/jasperserver/files/JasperServer/JasperReports%20Server%20Community%20Edition%206.1.1/jasperreports-
server-cp-6.1.1-bin.zip -o /tmp/jasperserver.zip && \  
unzip /tmp/jasperserver.zip -d /usr/src/ && \  
mv /usr/src/jasperreports-server-cp-6.1.1-bin /usr/src/jasperreports-server &&
\  
rm -rf /tmp/*  
  
# Install JDK and set JAVA_HOME to prepare for js-ant build  
RUN apt-get update && apt-get install -y -q openjdk-7-jdk && rm -rf
/var/lib/apt/lists/*  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/  
  
# TODO: Allow using different db backends for open source  
COPY postgresql_master.properties /usr/src/jasperreports-
server/buildomatic/default_master.properties  
COPY postgresql/postgresql-9.4-1201.jdbc4.jar /usr/src/jasperreports-
server/buildomatic/conf_source/db/postgresql/jdbc/  
COPY postgresql/db.template.properties /usr/src/jasperreports-
server/buildomatic/conf_source/db/postgresql/  
  
# Only build the webapp part, the DB should be done separately before running
container using db-initialization.sh  
# (see README)  
RUN cd /usr/src/jasperreports-server/buildomatic && ./js-ant deploy-webapp-ce  
  
# Cleanup tomcat stuff to only have jasperreports server at root  
RUN rm -rf /usr/local/tomcat/webapps/ROOT && \  
rm -rf /usr/local/tomcat/webapps/docs && \  
rm -rf /usr/local/tomcat/webapps/examples && \  
rm -rf /usr/local/tomcat/webapps/host-manager && \  
rm -rf /usr/local/tomcat/webapps/manager && \  
mv /usr/local/tomcat/webapps/jasperserver /usr/local/tomcat/webapps/ROOT && \  
sed -i "s/jasperserver\\.root/ROOT.root/g" /usr/local/tomcat/webapps/ROOT/WEB-
INF/web.xml && \  
sed -i "s/jasperserver\\.root/ROOT.root/g" /usr/local/tomcat/webapps/ROOT/WEB-
INF/log4j.properties  
  
# the Docker healthcheck command ~ at first start-up it will be "starting"
until the Tomcat app is deployed and ready  
HEALTHCHECK CMD curl --fail http://localhost:8080/login.html || exit 1  
  
# Use an entrypoint to do env var to DB setting translation  
COPY entrypoint.sh /  
COPY db-initialize.sh /usr/local/bin/db-initialize.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["catalina.sh", "run"]  

