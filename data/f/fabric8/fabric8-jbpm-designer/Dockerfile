FROM centos:centos6  
  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
# install Java 7  
RUN yum -y install java-1.7.0-openjdk mysql-server mysql install git ant wget;
yum clean all  
  
ENV JBPM_VERSION 6.2.0.Final  
ENV JBPM_HOME /opt/jbpm  
  
RUN wget -nv
http://ufpr.dl.sourceforge.net/project/jbpm/jBPM%206/jbpm-${JBPM_VERSION}/jbpm-${JBPM_VERSION}-installer-
full.zip -O /tmp/jbpm-${JBPM_VERSION}-installer-full.zip  
RUN yum install -y unzip  
  
RUN unzip -q /tmp/jbpm-${JBPM_VERSION}-installer-full.zip -d ${JBPM_HOME} &&
rm /tmp/jbpm-${JBPM_VERSION}-installer-full.zip  
  
ADD config/standalone-full-wildfly-8.1.0.Final.xml /opt/jbpm/jbpm-installer/  
ADD config/build.properties /opt/jbpm/jbpm-installer/  
ADD config/jbpm-persistence-JPA2.xml /opt/jbpm/jbpm-installer/db/  
  
WORKDIR /opt/jbpm/jbpm-installer/  
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/  
RUN ant install.demo.noeclipse  
  
ADD configure_mysql.sh /tmp/  
RUN /tmp/configure_mysql.sh && rm /tmp/configure_mysql.sh  
  
EXPOSE 8080  
RUN mv /opt/jbpm/jbpm-
installer/wildfly-8.1.0.Final/standalone/deployments/jbpm-console.war
/opt/jbpm/jbpm-installer/wildfly-8.1.0.Final/standalone/deployments/ROOT.war  
ADD start.sh /  
  
# wildfly module.xml refers to jar without version in the name  
RUN mv /opt/jbpm/jbpm-
installer/wildfly-8.1.0.Final/modules/com/mysql/main/mysql-connector-
java-5.1.18.jar /opt/jbpm/jbpm-
installer/wildfly-8.1.0.Final/modules/com/mysql/main/mysql-connector-java.jar  
  
# lets populate a default workflow example  
ADD workflows /opt/jbpm/examples/workflows  
WORKDIR /opt/jbpm/examples/workflows  
RUN git config --global user.name "fabric8" && git config --global user.email
fabric8@googlegroups.com && \  
git init && git add * */.gitignore && git commit -m "Initial import"  
  
CMD /start.sh  

