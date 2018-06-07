FROM jboss/wildfly  
  
# git install  
USER root  
RUN yum install -y
http://mirror.centos.org/centos-7/7/os/x86_64/Packages/git-1.8.3.1-4.el7.x86_64.rpm  
USER jboss  
# java config  
ADD jdk-8u65-linux-x64.tar.gz /opt/java/  
ENV PATH=$PATH:/opt/java/jdk1.8.0_65/bin  
ENV JAVA_HOME=/opt/java/jdk1.8.0_65/  
  
# maven config  
ADD apache-maven-3.3.3-bin.tar.gz /opt/maven/  
#CMD tar -xzf /opt/maven/apache-maven-3.3.3-bin.tar.gz  
ENV M2_HOME /opt/maven/apache-maven-3.3.3  
ENV PATH=$PATH:/opt/maven/apache-maven-3.3.3/bin  
  
# gradle config  
ADD gradle-2.8.tar.gz /opt/gradle/  
#CMD tar xzf /opt/gradle/gradle-2.8.tar.gz  
ENV GRADLE_HOME /opt/gradle/gradle-2.8  
ENV PATH=$PATH:/opt/gradle/gradle-2.8/bin  
  
# jenkins config  
USER root  
RUN mkdir /opt/jenkins_home && chown -R jboss:jboss /opt/jenkins_home  
USER jboss  
ENV JENKINS_HOME /opt/jenkins_home  
ADD jenkins.war /opt/jboss/wildfly/standalone/deployments/  
ADD bitbucket-hook-manager-1.0.3.war
/opt/jboss/wildfly/standalone/deployments/  

