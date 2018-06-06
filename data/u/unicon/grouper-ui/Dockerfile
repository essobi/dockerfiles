FROM unicon/grouper-web-base:2.3.0  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
COPY patch-scripts/ /opt/patch-scripts/  
COPY grouper-ui/ /opt/grouper.ui-$GROUPER_VERSION/  
  
RUN yum update -y \  
&& yum install -y wget tar \  
&& yum clean all \  
\  
&& echo 'Downloading grouper UI...' \  
&& wget -q
http://software.internet2.edu/grouper/release/$GROUPER_VERSION/grouper.ui-$GROUPER_VERSION.tar.gz
\  
&& tar -zxf grouper.ui-$GROUPER_VERSION.tar.gz \--skip-old-files -C /opt \  
\  
&& cd /opt/grouper.ui-$GROUPER_VERSION \  
&& /opt/apache-ant-1.9.5/bin/ant war \  
&& cp dist/grouper.war /opt/apache-tomcat-6.0.44/webapps \  
\  
&& mkdir /opt/apache-tomcat-6.0.44/webapps/grouper/ \  
&& cd /opt/apache-tomcat-6.0.44/webapps/grouper \  
&& $JAVA_HOME/bin/jar xvf ../grouper.war \  
&& rm ../grouper.war \  
\  
&& echo 'Patching Grouper UI...'\  
&& mkdir /tmp/grp-ui/ \  
&& cd / \  
&& cp /opt/grouper.apiBinary-$GROUPER_VERSION/grouperPatchStatus.properties
/opt/apache-tomcat-6.0.44/webapps/grouper/WEB-INF/ \  
&& cp /opt/patch-scripts/grouper.installer-ui.properties
/grouper.installer.properties \  
&& $JAVA_HOME/bin/java -cp .:/opt/grouperInstaller.jar
edu.internet2.middleware.grouperInstaller.GrouperInstaller \  
\  
&& rm -rf grouper.ui-$GROUPER_VERSION.tar.gz /tmp/grp-ui/
/grouper.installer.properties  

