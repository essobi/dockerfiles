FROM unicon/grouper-web-base:2.3.0  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
COPY patch-scripts/ /opt/patch-scripts/  
COPY grouper-ws/ /opt/grouper.ws-$GROUPER_VERSION/grouper-ws/  
  
RUN yum update -y \  
&& yum install -y wget tar \  
&& yum clean all \  
\  
&& echo 'Downloading grouper Web Services...' \  
&& wget -q
http://software.internet2.edu/grouper/release/$GROUPER_VERSION/grouper.ws-$GROUPER_VERSION.tar.gz
\  
&& tar -zxf grouper.ws-$GROUPER_VERSION.tar.gz --skip-old-files -C /opt \  
\  
&& cd /opt/grouper.ws-$GROUPER_VERSION/grouper-ws/ \  
&& /opt/apache-ant-1.9.5/bin/ant dist \  
&& cp build/dist/grouper-ws.war /opt/apache-tomcat-6.0.44/webapps \  
\  
&& mkdir /opt/apache-tomcat-6.0.44/webapps/grouper-ws/ \  
&& cd /opt/apache-tomcat-6.0.44/webapps/grouper-ws \  
&& $JAVA_HOME/bin/jar xvf ../grouper-ws.war \  
&& rm ../grouper-ws.war \  
\  
&& echo 'Patching Grouper WS...'\  
&& mkdir /tmp/grp-ws/ \  
&& cd / \  
&& cp /opt/grouper.apiBinary-$GROUPER_VERSION/grouperPatchStatus.properties
/opt/apache-tomcat-6.0.44/webapps/grouper-ws/WEB-INF/ \  
&& cp /opt/patch-scripts/grouper.installer-ws.properties
/grouper.installer.properties \  
&& $JAVA_HOME/bin/java -cp .:/opt/grouperInstaller.jar
edu.internet2.middleware.grouperInstaller.GrouperInstaller \  
\  
&& rm -rf grouper.ws-$GROUPER_VERSION.tar.gz /tmp/grp-ws/
/grouper.installer.properties  

