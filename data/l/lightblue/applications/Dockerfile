FROM paterczm/docker-fedora20-jbossas7  
MAINTAINER Marek Paterczyk <paterczm@users.noreply.github.com>  
  
ENV METADATA_APP_VERSION 1.2.0  
ENV DATA_APP_VERSION 1.2.0  
ENV JBOSS_HOME=/opt/jbossas7  
  
RUN curl -o $JBOSS_HOME/standalone/deployments/metadata.war
https://repo1.maven.org/maven2/com/redhat/lightblue/applications/lightblue-
applications-metadata-mgmt/1.2.0/lightblue-applications-metadata-
mgmt-$METADATA_APP_VERSION.war  
RUN curl -o $JBOSS_HOME/standalone/deployments/data.war
https://repo1.maven.org/maven2/com/redhat/lightblue/applications/lightblue-
applications-data-mgmt/1.2.0/lightblue-applications-data-
mgmt-$DATA_APP_VERSION.war  
  
RUN mkdir -p $JBOSS_HOME/modules/com/redhat/lightblue/main  
ADD lightblue_config $JBOSS_HOME/modules/com/redhat/lightblue/main/  

