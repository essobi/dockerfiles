FROM centos:centos7  
  
MAINTAINER Eduardo Souza  
  
# Installs core modules  
RUN yum -y update && yum -y install wget git && yum -y clean all  
  
# Installs JDK 8  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jre-8u11-linux-x64.rpm"
-O /opt/jre-8u11-linux-x64.rpm  
RUN rpm -Uvh /opt/jre-8u11-linux-x64.rpm && rm /opt/jre-8u11-linux-x64.rpm  
  
ADD http://mirrors.jenkins-ci.org/war/latest/jenkins.war /opt/jenkins.war  
  
RUN mkdir -p /home/jenkins  
RUN useradd --user-group --system --home-dir /home/jenkins jenkins  
RUN chown -R jenkins:jenkins /home/jenkins /opt/jenkins.war  
ENV JENKINS_HOME /home/jenkins  
VOLUME ["/home/jenkins"]  
  
EXPOSE 8080  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
CMD /usr/local/bin/run  

