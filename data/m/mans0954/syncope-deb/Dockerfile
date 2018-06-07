# Don't use stock tomcat container, as it doesn't use the tomcat package  
# which the syncope packages depend on  
FROM debian  
MAINTAINER christopher.hoskin@gmail.com  
  
# Install Tomcat  
RUN apt-get update && apt-get install -y tomcat8 libservlet3.1-java  
EXPOSE 8080  
# Set up Postgresql driver  
RUN apt-get install -y libpostgresql-jdbc-java  
RUN ln -s /usr/share/java/postgresql-jdbc4.jar /usr/share/tomcat8/lib/  
# Install Postgresql client (useful for debug)  
RUN apt-get install -y postgresql-client  
  
# Install Apache Syncope  
ENV syncope_version 2.0.7  
RUN apt-get install -y wget  
RUN wget
http://mirror.ox.ac.uk/sites/rsync.apache.org/syncope/${syncope_version}/apache-
syncope-${syncope_version}.deb  
RUN wget
http://mirror.ox.ac.uk/sites/rsync.apache.org/syncope/${syncope_version}/apache-
syncope-console-${syncope_version}.deb  
RUN wget
http://mirror.ox.ac.uk/sites/rsync.apache.org/syncope/${syncope_version}/apache-
syncope-enduser-${syncope_version}.deb  
RUN dpkg -i apache-syncope-*.deb  
RUN rm apache-syncope-*.deb  
  
# Wire up Syncope to use the postgres-syncope container  
RUN sed -i
's|Master.url=jdbc:postgresql://localhost:5432/syncope|Master.url=jdbc:postgresql://postgres:5432/syncope|'
\  
/etc/apache-syncope/domains/Master.properties  
COPY syncope.xml /etc/tomcat8/Catalina/localhost/syncope.xml  
RUN chown tomcat8:tomcat8 /etc/tomcat8/Catalina/localhost/syncope.xml  
  
# Add connector server  
ADD connid.properties /etc/apache-syncope/connid.properties  
  
USER tomcat8  
RUN mkdir /tmp/tomcat8-tomcat8-tmp  
#ENV JAVA_OPTS="-Djava.awt.headless=true -Dfile.encoding=UTF-8 -server \  
# -Xms1536m -Xmx1536m -XX:NewSize=256m -XX:MaxNewSize=256m \  
# -XX:PermSize=256m -XX:MaxPermSize=256m -XX:+DisableExplicitGC"  
CMD ["/usr/lib/jvm/default-java/bin/java", \  
"-Djava.util.logging.config.file=/var/lib/tomcat8/conf/logging.properties", \  
"-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager", \  
"-Djava.awt.headless=true", \  
"-Dfile.encoding=UTF-8", \  
"-server", \  
"-Xms1536m", \  
"-Xmx1536m", \  
"-XX:NewSize=256m", \  
"-XX:MaxNewSize=256m", \  
"-XX:PermSize=256m", \  
"-XX:MaxPermSize=256m", \  
"-XX:+DisableExplicitGC", \  
"-Djava.endorsed.dirs=/usr/share/tomcat8/endorsed", \  
"-classpath",
"/usr/share/tomcat8/bin/bootstrap.jar:/usr/share/tomcat8/bin/tomcat-juli.jar",
\  
"-Dcatalina.base=/var/lib/tomcat8", \  
"-Dcatalina.home=/usr/share/tomcat8", \  
"-Djava.io.tmpdir=/tmp/tomcat8-tomcat8-tmp", \  
"org.apache.catalina.startup.Bootstrap", \  
"start"]  
  

