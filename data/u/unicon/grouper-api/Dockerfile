FROM unicon/grouper-java-base:7u95  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
ENV GROUPER_VERSION=2.3.0  
  
COPY patch-scripts/ /opt/patch-scripts/  
  
RUN yum update -y \  
&& yum install -y wget tar \  
&& yum clean all \  
\  
&& echo 'Downloading Grouper Installer...' \  
&& wget -q
http://software.internet2.edu/grouper/release/$GROUPER_VERSION/grouperInstaller.jar
\  
&& mv grouperInstaller.jar /opt/ \  
\  
&& echo 'Downloading Grouper API...'\  
&& wget -q
http://software.internet2.edu/grouper/release/$GROUPER_VERSION/grouper.apiBinary-$GROUPER_VERSION.tar.gz
\  
&& tar -zxf grouper.apiBinary-$GROUPER_VERSION.tar.gz -C /opt \  
\  
&& echo 'Patching Grouper API...'\  
&& mkdir /tmp/grp-api/ \  
&& cp /opt/patch-scripts/grouper.installer-api.properties
/grouper.installer.properties \  
&& $JAVA_HOME/bin/java -cp .:/opt/grouperInstaller.jar
edu.internet2.middleware.grouperInstaller.GrouperInstaller \  
\  
&& rm -rf grouper.apiBinary-$GROUPER_VERSION.tar.gz /tmp/grp-api/
/grouper.installer.properties  

