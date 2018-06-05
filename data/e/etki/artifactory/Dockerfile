FROM java:8-alpine  
  
EXPOSE 80 8091  
  
RUN wget -q -O /tmp/artifactory.zip \  
https://bintray.com/artifact/download/jfrog/artifactory/jfrog-artifactory-
oss-4.5.2.zip && \  
unzip /tmp/artifactory.zip -d /tmp && mv /tmp/artifactory-oss-4.5.2
/var/lib/artifactory && \  
rm /tmp/artifactory.zip  
  
ENV ARTIFACTORY_HOME=/var/lib/artifactory TOMCAT_HOME=/var/lib/tomcat  
ENV CATALINA_OPTS="$JAVA_OPTIONS -Dartifactory.home=$ARTIFACTORY_HOME
-Dfile.encoding=UTF8 -Djruby.compile.invokedynamic=false"  
# Creating a little bit more pleasant layout  
RUN mv /var/lib/artifactory/tomcat /var/lib/tomcat && \  
rm -rf /var/lib/tomcat/webapps/ROOT && \  
mv /var/lib/artifactory/webapps/artifactory.war
/var/lib/artifactory/artifactory.war && \  
mv /var/lib/tomcat/conf/Catalina/localhost/artifactory.xml
/var/lib/tomcat/conf/Catalina/localhost/ROOT.xml  
# Configuration  
RUN sed -i.bak 's:<Connector port="8081"/>:<Connector port="80"/>:g'
/var/lib/tomcat/conf/server.xml && \  
sed -i.bak 's:<Context path=".*" docBase=".*">:<Context path=""
docBase="/var/lib/artifactory/artifactory.war">:g'
/var/lib/tomcat/conf/Catalina/localhost/ROOT.xml  
  
CMD ["/var/lib/tomcat/bin/catalina.sh", "run"]

