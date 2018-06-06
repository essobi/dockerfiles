FROM unicon/grouper-api:2.2.2  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
ENV GROUPER_VERSION=2.2.2  
COPY patch-scripts/ /opt/patch-scripts/  
  
RUN yum update -y \  
&& yum install -y wget tar \  
&& yum clean all \  
\  
&& echo 'Downloading Grouper PSP...'\  
&& wget -q
http://software.internet2.edu/grouper/release/$GROUPER_VERSION/grouper.psp-$GROUPER_VERSION.tar.gz
\  
&& tar -zxf grouper.psp-$GROUPER_VERSION.tar.gz -C /opt \  
&& cp -R /opt/grouper.psp-$GROUPER_VERSION/lib/custom/*
/opt/grouper.apiBinary-$GROUPER_VERSION/lib/custom \  
\  
&& echo 'Patching Grouper PSP...'\  
&& mkdir /tmp/grp-psp/ \  
&& cp /opt/patch-scripts/grouper.installer-psp.properties
/grouper.installer.properties \  
&& $JAVA_HOME/bin/java -cp .:/opt/grouperInstaller.jar
edu.internet2.middleware.grouperInstaller.GrouperInstaller \  
\  
&& rm -rf grouper.psp-$GROUPER_VERSION.tar.gz /tmp/grp-psp/
/grouper.installer.properties  
  
WORKDIR /opt/grouper.apiBinary-$GROUPER_VERSION/  
  
CMD ["/bin/sh", "bin/gsh", "-loader"]  
  

