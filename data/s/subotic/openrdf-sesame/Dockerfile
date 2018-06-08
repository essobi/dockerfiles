FROM centos:7  
MAINTAINER Ivan Subotic "ivan.subotic@unibas.ch"  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.30  
ENV CATALINA_HOME /tomcat  
ENV CATALINA_BASE /tomcat  
ENV SESAME_VERSION 2.8.7  
ENV SESAME_DATA /data  
ENV JAVA_MAXMEMORY 4096  
# IMPORT the Centos-7 GPG key to prevent warnings  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7  
  
# Add bintray repository where the SBT binaries are published  
RUN curl -sS https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-
sbt-rpm.repo  
  
# Base Install + JDK + SBT  
RUN yum -y update && \  
yum -y install java-1.8.0-openjdk && \  
yum -y install java-1.8.0-openjdk-devel && \  
yum -y install sbt && \  
yum -y update bash && \  
rm -rf /var/cache/yum/* && \  
yum clean all  
  
# Run SBT once so that all libraries are downloaded  
RUN sbt exit  
  
# Install Tomcat  
RUN curl -sS -O
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
curl -sS
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME}  
  
# Remove docs and examples  
RUN rm -rf $CATALINA_BASE/webapps/docs && \  
rm -rf $CATALINA_BASE/webapps/examples  
  
# Install Sesame  
RUN curl -sS -o /tmp/sesame.tar.gz -L
http://sourceforge.net/projects/sesame/files/Sesame%202/$SESAME_VERSION/openrdf-
sesame-$SESAME_VERSION-sdk.tar.gz/download && \  
tar -xzf /tmp/sesame.tar.gz -C /opt && \  
ln -s /opt/openrdf-sesame-$SESAME_VERSION /opt/sesame && \  
rm /tmp/sesame.tar.gz  
  
# Deploy  
RUN mkdir ${CATALINA_BASE}/webapps/openrdf-sesame && \  
cd ${CATALINA_BASE}/webapps/openrdf-sesame && \  
jar xf /opt/sesame/war/openrdf-sesame.war && \  
mkdir ${CATALINA_BASE}/webapps/openrdf-workbench && \  
cd ${CATALINA_BASE}/webapps/openrdf-workbench && \  
jar xf /opt/sesame/war/openrdf-workbench.war  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 8080  
CMD ["/run.sh"]

