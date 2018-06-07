# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Salvador Rodriguez <salvador.rodriguez@utah.edu>  
  
# Install packages  
ENV REFRESHED_AT 2015-03-27  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install wget pwgen unzip && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Java  
RUN \  
apt-get update && \  
apt-get install -y openjdk-7-jre && \  
rm -rf /var/lib/apt/lists/*  
  
# Set java home  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
RUN echo PATH=$JAVA_HOME/bin:$PATH:$HOME/bin >> ~/.bashrc  
RUN echo export PATH JAVA_HOME >> ~/.bashrc  
  
# Install Tomcat  
ENV TOMCAT_MAJOR_VERSION 6  
ENV TOMCAT_MINOR_VERSION 0.43  
RUN wget
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MAJOR_VERSION}.${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MAJOR_VERSION}.${TOMCAT_MINOR_VERSION}.zip  
RUN unzip apache-tomcat-${TOMCAT_MAJOR_VERSION}.${TOMCAT_MINOR_VERSION}.zip  
RUN rm -f apache-tomcat-${TOMCAT_MAJOR_VERSION}.${TOMCAT_MINOR_VERSION}.zip  
RUN mv /apache-tomcat-${TOMCAT_MAJOR_VERSION}.${TOMCAT_MINOR_VERSION} /tomcat  
ADD tomcat-users.xml /tomcat/conf/tomcat-users.xml  
ADD setenv.sh /tomcat/bin/setenv.sh  
RUN cd /tomcat/bin/; chmod +x *.sh  
  
# Add guvnor  
ENV DROOLS_VERSION 5.6.0.Final  
  
RUN wget http://download.jboss.org/drools/release/${DROOLS_VERSION}/guvnor-
distribution-${DROOLS_VERSION}.zip -O /tmp/guvnor-
distribution-${DROOLS_VERSION}.zip && \  
unzip -q /tmp/guvnor-distribution-${DROOLS_VERSION}.zip -d /tmp/ && \  
chown -R 501:501 /tmp/guvnor-distribution-${DROOLS_VERSION}/ && \  
cd /tomcat/webapps/ && \  
mv /tmp/guvnor-
distribution-${DROOLS_VERSION}/binaries/guvnor-${DROOLS_VERSION}-tomcat-6.*.war
./drools-guvnor.war && \  
cd / && \  
rm -rf /tmp/* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN unzip /tomcat/webapps/drools-guvnor.war -d tomcat/webapps/drools-guvnor  
RUN rm /tomcat/webapps/drools-guvnor.war  
  
# Add opencds-common jar  
ADD opencds-common.jar /tomcat/webapps/drools-guvnor/WEB-INF/lib/opencds-
common.jar  
  
# Add designer  
RUN wget
http://sourceforge.net/projects/jbpm/files/designer/designer-2.4/jbpm-
designer-2.4.0.Final-tomcat.war  
RUN mv jbpm-designer-2.4.0.Final-tomcat.war /tomcat/webapps/designer.war  
  
# Add opencds-guvnor.properties  
ADD opencds-guvnor.properties /root/.opencds/opencds-guvnor.properties  
  
EXPOSE 8080  
CMD ["/tomcat/bin/catalina.sh", "run"]  

