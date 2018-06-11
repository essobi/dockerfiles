FROM centos  
  
MAINTAINER Utsav Kumar <utsav2307@gmail.com>  
  
ENV JENKINS_HOME=/jenkins  
  
RUN yum update -y && \  
yum install -y wget && \  
yum install -y java && \  
mkdir /jenkins && \  
mkdir /tomcat  
  
RUN cd tomcat && \  
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.0.M1/bin/apache-
tomcat-9.0.0.M1.tar.gz && \  
tar -xzf apache-tomcat-9.0.0.M1.tar.gz && \  
mv apache-tomcat-9.0.0.M1/* . && \  
rm -rf apache-tomcat-9.0.0.M1.tar.gz apache-tomcat-9.0.0.M1 && \  
cd /tomcat/webapps && \  
wget http://updates.jenkins-ci.org/download/war/2.32.2/jenkins.war  
  
VOLUME ["${JENKINS_HOME}"]  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh && chmod -R ug+rwx /jenkins  
ENTRYPOINT ["/bin/bash", "-c", "/start.sh"]  
CMD ["echo", "started"]  

